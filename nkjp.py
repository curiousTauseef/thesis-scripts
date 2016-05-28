#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import re
import string

prefix = '{http://www.tei-c.org/ns/1.0}'

def remove_nonalpha(string):
    pattern = re.compile('[\W_]+', re.UNICODE)
    return pattern.sub('', string)

def contract_whitespace(string):
    pattern = re.compile('\s+')
    return pattern.sub(' ', string)

def is_num(string):
    roman = ['ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    return string in roman or any(char.isdigit() for char in string)

def parse(filename):
    root = xml.etree.ElementTree.parse(filename).getroot()
    for sentence in root.findall(".//{0}s".format(prefix)):
        out = []
        for segment in sentence.findall(".//{0}seg".format(prefix)): 
            orth = segment.find(".//{0}f[@name='orth']/{0}string".format(prefix)).text
            interpretation = segment.find(".//{0}f[@name='interpretation']/{0}string".format(prefix)).text.split(':')
            base = interpretation[0]
            pos = interpretation[1]
            if pos == 'num' or is_num(orth):
                out.append('num')
            if pos == 'aglt':
                print("KURWAA{}\n\n".format(orth))
                break
            elif pos not in ['brev', 'ign', 'interp', 'xxx']:
                out.append(pattern.sub('', orth.lower()))
        if len(out) > 4 and out.count('num') < 3:
            print(re.sub(r'\s+', ' ', ' '.join(out)))

path = '/media/sebastian/Seagate Expansion Drive/mgr/nkjp/misc'
for filename in glob.iglob(path + '/**/ann_morphosyntax.xml', recursive=True):
    parse(filename)
