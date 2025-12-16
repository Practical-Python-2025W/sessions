from utils import relative_path_resolver
import os
import glob
from lxml import etree as ET
import spacy

########################################################
# I don't take any responsibility for the code below   #
# or for the contents you might process while running  #
# it.                                                  #
#            Use at your own risk!                     # 
########################################################

# configuration
DATA_DIR = relative_path_resolver("../data/")
INPUT_DIR = os.path.join(DATA_DIR, "extracted_articles/")
OUTPUT_DIR = os.path.join(DATA_DIR, "pos_tagged_articles/")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load spaCy model (download with: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")


def split_into_paragraphs(text):
    """Split text into paragraphs based on newlines."""
    paragraphs = text.split('\n')
    return [p.strip() for p in paragraphs if p.strip()]


def process_paragraph(paragraph_text):
    """Tokenize and POS tag a paragraph using spaCy."""
    doc = nlp(paragraph_text)
    return doc


def enhance_xml(input_path, output_path):
    """Read XML, add paragraph and POS tagging, save enhanced XML."""
    # Parse the input XML
    tree = ET.parse(input_path)
    root = tree.getroot()
    text_element = root.find('.//body/text')
    original_text = text_element.text
    text_element.text = None
    text_element.clear()
    paragraphs = split_into_paragraphs(original_text)
    for para_text in paragraphs:
        p_element = ET.SubElement(text_element, "p")
        doc = process_paragraph(para_text)
        for i, token in enumerate(doc):
            w_element = ET.SubElement(p_element, "w")
            w_element.set("pos", token.pos_)
            w_element.text = token.text
            # Add space after token if not the last one and if there's a space
            if i < len(doc) - 1 and token.whitespace_:
                w_element.tail = " "
    tree.write(output_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    print(f"writing: {os.path.basename(output_path)}")


def process_all_xml_files():
    """Process all XML files in the input directory."""
    xml_files = glob.glob(os.path.join(INPUT_DIR, "*.xml"))
    print(f"Found {len(xml_files)} XML files to process...")
    prefix = "pos_"
    for input_path in xml_files:
        filename = os.path.basename(input_path)
        output_path = os.path.join(OUTPUT_DIR, prefix + filename)
        try:
            enhance_xml(input_path, output_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    print(f"Done! Processed files saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    process_all_xml_files()
