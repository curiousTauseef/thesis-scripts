#requires Python >= 3.5
import xml.etree.ElementTree
import glob

prefix = '{http://www.tei-c.org/ns/1.0}'
def parse(filename):
    root = xml.etree.ElementTree.parse(filename).getroot()
    for sentence in root.findall(".//{0}s".format(prefix)):
        out = []
        for segment in sentence.findall(".//{0}seg".format(prefix)): 
            orth = segment.find(".//{0}f[@name='orth']/{0}string".format(prefix))
            interpretation = segment.find(".//{0}f[@name='interpretation']/{0}string".format(prefix))
            base = interpretation.text.split(':')[0]
            pos = interpretation.text.split(':')[1]
            if pos in ['num', 'ign']:
                out.append(pos)
                print("KURWWAAAAAAA\n\n\n{0}".format(orth.text))
            elif pos not in ['brev', 'interp', 'xxx', 'aglt']:
                out.append(orth.text.lower())
        if len(out) > 4:
            print(' '.join(out))

path = '/media/sebastian/Seagate Expansion Drive/mgr/free/4/IJP/'
for filename in glob.iglob(path + '/**/ann_morphosyntax.xml', recursive=True):
    parse(filename)
