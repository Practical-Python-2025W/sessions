# Add a # character in front of every uppercase letter.
# • Make sure the # is added only to text content, not inside
# XML tags.
# • Identify cases where the change must be made only using
# the plain-text version, rather than by directly modifying
# the XML string.

import simple_parser

for xml_file in simple_parser.input_path.glob("*.xml"):
    ptxt = simple_parser.Plaintexter(xml_file)
    ptxt.parse()
    plain_text = ptxt.plain_text
    print(ptxt.xml_string)
    mapping = ptxt.mapping

    insert_positions = []
    for plain_idx, xml_idx in mapping.items():
        if plain_text[plain_idx].isupper():
            insert_positions.append(xml_idx)

    # Insert '#' directly into the XML string at those positions.
    # Process from right to left so indices stay valid as we insert.
    xml_chars = list(ptxt.xml_string)
    for xml_idx in sorted(insert_positions, reverse=True):
        xml_chars.insert(xml_idx, '#')

    new_xml_string = ''.join(xml_chars)
    print(f"--- {xml_file.name} ---")
    print(new_xml_string)