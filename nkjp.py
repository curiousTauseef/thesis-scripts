#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import re
import string

prefix = '{http://www.tei-c.org/ns/1.0}'
sentences = ".//{0}s".format(prefix)
segments = ".//{0}seg".format(prefix)
orthographic = ".//{0}f[@name='orth']/{0}string".format(prefix)
interpretation = ".//{0}f[@name='interpretation']/{0}string".format(prefix)

def remove_nonalpha(string):
    pattern = re.compile('[\W_]+', re.UNICODE)
    return pattern.sub('', string)

def contract_whitespace(string):
    pattern = re.compile('\s+')
    return pattern.sub(' ', string)

def is_num(string):
    roman = ['ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    return string in roman or any(char.isdigit() for char in string)

def is_valid(line):
    return len(line) > 4 and out.count('num') < 4

def parse(filename):
    root = xml.etree.ElementTree.parse(filename).getroot()
    for sentence in root.findall(sentences):
        line = []
        for segment in sentence.findall(segments): 
            orth = segment.find(orthographic).text.lower()
            interp = segment.find(interpretation).text.lower().split(':')
            base = interp[0]
            pos = interp[1]
            if pos == 'num' or is_num(orth):
                line.append('num')
            elif pos == 'aglt':
                print("KURWAA{}\n\n".format(orth))
                break
            elif pos not in ['brev', 'ign', 'interp', 'xxx']:
                line.append(remove_nonalpha(orth))
        if is_valid(line):
            print(contract_whitespace(' '.join(line)))

path = '/media/sebastian/Seagate Expansion Drive/mgr/nkjp/misc'
for filename in glob.iglob(path + '/**/ann_morphosyntax.xml', recursive=True):
    parse(filename)
