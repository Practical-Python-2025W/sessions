from utils import relative_path_resolver
import os
import gzip
import requests
from warcio.archiveiterator import ArchiveIterator
import trafilatura
from lxml import etree as ET
from langdetect import detect, LangDetectException

########################################################
# I don't take any responsibility for the code below   #
# or for the contents you might download while running #
# it.                                                  #
#            Use at your own risk!                     # 
########################################################

# configuration
DATA_DIR = relative_path_resolver("../data/")
# from https://data.commoncrawl.org/crawl-data/CC-NEWS/2025/index.html :
WARC_PATHS_FILE = os.path.join(DATA_DIR, "warc.paths")
OUTPUT_DIR = os.path.join(DATA_DIR, "extracted_articles/")
LOCAL_WARC = os.path.join(DATA_DIR, "sample.warc.gz")
WARC_BASE_URL = "https://data.commoncrawl.org/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_warc_urls():
    """Load WARC URLs from the paths file."""
    with open(WARC_PATHS_FILE) as f:
        for line in f.readlines():
            yield WARC_BASE_URL + line.strip()

def download_warcs():
    """Download WARC files from the list of URLs."""
    for warc_url in load_warc_urls():
        print(f"Downloading WARC file {warc_url}")
        with requests.get(warc_url, stream=True) as r:
            r.raise_for_status()
            with open(LOCAL_WARC, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        break


def make_xml(doc_id, metadata, text):
    """Build a minimal XML structure."""
    root = ET.Element("article")
    meta = ET.SubElement(root, "meta")
    ET.SubElement(meta, "id").text = str(doc_id)
    ET.SubElement(meta, "url").text = metadata.url or ""
    ET.SubElement(meta, "title").text = metadata.title or ""
    ET.SubElement(meta, "domain").text = metadata.sitename or ""
    ET.SubElement(meta, "author").text = metadata.author or ""
    ET.SubElement(meta, "date").text = metadata.date or ""
    ET.SubElement(meta, "description").text = metadata.description or ""
    categories = ET.SubElement(meta, "categories")
    if metadata.categories:
        for cat in metadata.categories:
            ET.SubElement(categories, "category").text = cat
    body = ET.SubElement(root, "body")
    ET.SubElement(body, "text").text = text or ""
    return root


def delete_old_xml_files():
    """Delete old XML files in the output directory."""
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".xml"):
            os.remove(os.path.join(OUTPUT_DIR, filename))

def write_xml(doc_id, metadata, text):
    """Write the XML representation of the article to a file."""
    root = make_xml(doc_id, metadata, text)
    tree = ET.ElementTree(root)
    out_path = os.path.join(OUTPUT_DIR, f"article_{doc_id:05}.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    print(f"Saved {out_path}")

def process_record(record):
    """Process WARC record and extract articles."""
    if record.rec_type != "response":
        return None, None
    raw_bytes = record.content_stream().read()
    # Extract article text using trafilatura.
    # You never heard of that? Me neither!
    # But it looks promising for quick webscraping (prima facie).
    # Check it out if you want to know more: https://trafilatura.readthedocs.io/
    fail = None, None
    try:
        extracted = trafilatura.extract(
            raw_bytes.decode("utf-8", errors="ignore"),
            include_comments=False,
            include_tables=False
        )
    except Exception:
        return fail
    if not extracted:
        return fail
    try:
        lang = detect(extracted)
        if lang != 'en':
            return fail
    except LangDetectException:
        return fail
    metadata = trafilatura.extract_metadata(raw_bytes.decode("utf-8", errors="ignore"))
    if not metadata:
        return fail
    return metadata, extracted


def warc_urls_2_xml():    
    """download WARC files from warc URLs, convert to XML"""
    input("This will delete all old XML files in the output directory. Press Enter to continue or Ctrl-C to abort.")
    delete_old_xml_files()
    if not os.path.exists(LOCAL_WARC):
        download_warcs()
    doc_id = 1
    with gzip.open(LOCAL_WARC, "rb") as stream:
        for record in ArchiveIterator(stream):
            metadata, extracted = process_record(record)
            if metadata is None or extracted is None:
                continue
            write_xml(doc_id, metadata, extracted)
            doc_id += 1
    print(f"Done. Extracted {doc_id-1} articles.")
    
if __name__ == "__main__":
    warc_urls_2_xml()