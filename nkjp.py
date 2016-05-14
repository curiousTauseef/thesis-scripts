import xml.etree.ElementTree
root = xml.etree.ElementTree.parse('test.xml').getroot()
for segment in root.findall('.//{http://www.tei-c.org/ns/1.0}seg'):
    text = segment.find(".//{http://www.tei-c.org/ns/1.0}f[@name='orth']/{http://www.tei-c.org/ns/1.0}string")
    print(text.text)
