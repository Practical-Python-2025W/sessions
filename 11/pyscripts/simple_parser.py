"""script to turn simple XML files into plain text with index mapping.

It iterates over the text content in the xpathed XML element, builds a cleaned-up
plain-text version, and keeps a mapping so you can jump back to the
corresponding character positions in the original XML string.
"""

from pathlib import Path 
from lxml import etree

raw_input_dir: str = '../test_xml'
script_dir = Path(__file__).resolve().parent
input_path = script_dir / Path(raw_input_dir)

class Plaintexter:
    """Parse an XML file and get its specified elements' plain text.

    This class strips tags, normalises whitespace in a wonky way, and records a
    mapping between character indices in the resulting ``plain_text`` and
    their original positions in ``xml_string``.
    """

    text_container_xpath = "//body//text"
    opening_mark = "<"
    closing_mark = ">"
    ignored_whitespace_chars = ["\n", "\t", "\r"]
    no_whitespace_before = [";", ",", ":", ".", ")", "]", "}", "“"]
    no_whitespace_after = ["(", "[", "{", "„"]
    whitespace = " "
    single_quote = "'"
    double_quote = '"'
    indifferent_quotation_marks = [single_quote, double_quote]

    def __init__(self, xml_file: str, text_container_xpath: str | None = None):
        self.no_whitespace_after = self.no_whitespace_after.copy()
        self.no_whitespace_before = self.no_whitespace_before.copy()
        self.plain_text = ""
        if text_container_xpath:
            self.text_container_xpath = text_container_xpath
        self.mapping: dict[int, int] = {}
        self._load(xml_file)
        self.single_quotes_open = False
        self.double_quotes_open = False
    
    def plaintext_index_to_xml_index(self, plain_index: int) -> int:
        """Return the corresponding index in the original XML string.

        ``plain_index`` is an index in ``plain_text``.

        Raises ``KeyError`` if the index is out of bounds.
        """
        if self.mapping:
            return self.mapping[plain_index]
        else:
            raise KeyError("Mapping is empty; have you run parse() yet?")
        
    def xml_index_to_plaintext_index(self, xml_index: int) -> int:
        """Return the corresponding index in the plain text.

        ``xml_index`` is an index in ``xml_string``.

        Raises ``ValueError`` if the index is not found.
        """
        if self.mapping:
            for plain_index, mapped_xml_index in self.mapping.items():
                if mapped_xml_index == xml_index:
                    return plain_index
                raise ValueError(f"XML index {xml_index} not found in mapping.")
        else:
            raise ValueError("Mapping is empty; have you run parse() yet?")
        
    
    def _load(self, xml_file: str) -> None:
        """Internal helper that (re)loads the XML-related attributes.

        This manages the stuff we need in ``__init__`` and ``reload`` so we
        dont duplicate the parsing and attributes.
        """
        self.tree = etree.parse(xml_file)
        self.text_container = self.tree.xpath(self.text_container_xpath)[0]
        self.xml_string = etree.tostring(
            self.text_container,
            encoding='unicode',
            method='xml',  # keep tags!!!!
        )
        self.plain_text = ''
        self.mapping = {}
    
    def reload(self) -> None:
        """Reload the parser from file"""
        self._load(self.xml_file)
    
    def ignore_whitespace(self, char) -> bool: 
        if char == self.whitespace:
           if not self.plain_text:
               return True
           else:
               if self.plain_text[-1] == self.whitespace:
                    return True
               elif self.plain_text[-1] in self.no_whitespace_after:
                    return True
        return False
               
    def handle_quotation_marks(self, char) -> str:
        if char == self.single_quote:
            self.single_quotes_open = not self.single_quotes_open
            if self.single_quotes_open:
                self.no_whitespace_after.append(self.single_quote)
                if self.single_quote in self.no_whitespace_before:
                    self.no_whitespace_before.remove(self.single_quote)
            else:
                if self.single_quote in self.no_whitespace_after:
                    self.no_whitespace_after.remove(self.single_quote)
                self.no_whitespace_before.append(self.single_quote)
        elif char == self.double_quote:
            self.double_quotes_open = not self.double_quotes_open
            if self.double_quotes_open:
                self.no_whitespace_after.append(self.double_quote)
                if self.double_quote in self.no_whitespace_before:
                    self.no_whitespace_before.remove(self.double_quote)
            else:
                if self.double_quote in self.no_whitespace_after:
                    self.no_whitespace_after.remove(self.double_quote)
                self.no_whitespace_before.append(self.double_quote)
    
    def parse(self) -> None:
        """Builds ``plain_text`` and the mapping from the XML body.

        After calling this, ``plain_text`` contains the cleaned text and
        ``mapping`` links each plain-text index back to a position in
        ``xml_string``.
        """
        self.plain_text = ''
        tag_open = False
        self.mapping = {}
        plain_char_index = -1
        xml_char_index = -1
        for char in self.xml_string:
            xml_char_index += 1
            if char == self.opening_mark:
                tag_open = True
            elif char == self.closing_mark:
                tag_open = False
            else:
                if not tag_open:
                    if char in self.indifferent_quotation_marks:
                        self.handle_quotation_marks(char)
                    elif char in self.ignored_whitespace_chars:
                        char = self.whitespace
                    if not self.ignore_whitespace(char):
                        if (
                            char in self.no_whitespace_before and 
                            self.plain_text and 
                            self.plain_text[-1] == self.whitespace
                        ):
                            self.plain_text = self.plain_text[:-1]
                            plain_char_index -= 1
                        self.plain_text += char
                        plain_char_index += 1
                        self.mapping[plain_char_index] = xml_char_index
                else:
                    pass

        
    def test(self) -> None:
        """Debug helper that prints the mapping and the resulting text."""
        self.parse()
        print("Mapping:")
        for plain_char_i, xml_char_i in self.mapping.items():
            print(f"{self.plain_text[plain_char_i]} -> {self.xml_string[xml_char_i]}")
        print(self.plain_text)
    
def parse_all(input_path: Path, test: bool = False) -> None:
    """Parse all ``.xml`` files in the given folder.

    If ``test`` is True, each file runs through ``Plaintexter.test`` to
    show mapping, otherwise it just prints the plain text.
    """
    for xml_file in input_path.glob("*.xml"):
        parser = Plaintexter(xml_file)
        if test:
            parser.test()
        else:
            parser.parse()
        
if __name__ == "__main__":
    parse_all(input_path, test=True)