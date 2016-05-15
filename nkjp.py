import xml.etree.ElementTree

root = xml.etree.ElementTree.parse('test.xml').getroot()
for sentence in root.findall('.//{http://www.tei-c.org/ns/1.0}s'):
    out = []
    for segment in sentence.findall('.//{http://www.tei-c.org/ns/1.0}seg'): 
        text = segment.find(".//{http://www.tei-c.org/ns/1.0}f[@name='orth']/{http://www.tei-c.org/ns/1.0}string")
        out.append(text.text)
    print(' '.join(out))
