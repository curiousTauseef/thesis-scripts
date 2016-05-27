#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import re
import string

pattern = re.compile('[\W_]+', re.UNICODE)
prefix = '{http://www.tei-c.org/ns/1.0}'

def parse(filename):
    root = xml.etree.ElementTree.parse(filename).getroot()
    for sentence in root.findall(".//{0}s".format(prefix)):
        out = []
        for segment in sentence.findall(".//{0}seg".format(prefix)): 
            orth = segment.find(".//{0}f[@name='orth']/{0}string".format(prefix)).text
            interpretation = segment.find(".//{0}f[@name='interpretation']/{0}string".format(prefix)).text.split(':')
            base = interpretation[0]
            pos = interpretation[1]
            if pos in ['num', 'ign']:
                out.append(pos)
            elif pos not in ['brev', 'interp', 'xxx', 'aglt']:
                out.append(pattern.sub('', orth.lower()))
        if len(out) > 4:
            print(' '.join(out))

path = '/media/sebastian/Seagate Expansion Drive/mgr/nkjp/4/IJP/_internet/senat/xml/k5/60'
for filename in glob.iglob(path + '/**/ann_morphosyntax.xml', recursive=True):
    parse(filename)
