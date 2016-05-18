import xml.etree.ElementTree

root = xml.etree.ElementTree.parse('test.xml').getroot()
for sentence in root.findall('.//{http://www.tei-c.org/ns/1.0}s'):
    out = []
    for segment in sentence.findall('.//{http://www.tei-c.org/ns/1.0}seg'): 
        text = segment.find(".//{http://www.tei-c.org/ns/1.0}f[@name='orth']/{http://www.tei-c.org/ns/1.0}string")
        base = segment.find(".//{http://www.tei-c.org/ns/1.0}f[@name='base']/{http://www.tei-c.org/ns/1.0}string")
        pos = segment.find(".//{http://www.tei-c.org/ns/1.0}f[@name='interpretation']/{http://www.tei-c.org/ns/1.0}string")
        out.append(pos.text)
    print(' '.join(out))
