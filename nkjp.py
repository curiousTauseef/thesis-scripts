#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import os
import re
import string
import sys

prefix = '{http://www.tei-c.org/ns/1.0}'
sentences = ".//{0}s".format(prefix)
segments = ".//{0}seg".format(prefix)

gender = {'m1', 'm2', 'm3', 'f', 'n'}
number = {'pl', 'sg'}
case = {'nom', 'gen', 'dat', 'acc', 'inst', 'loc', 'voc'}

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
    return len(line) > 4 and line.count('num') < 3

def extract_orthographic(segment):
    tag = ".//{0}f[@name='orth']/{0}string".format(prefix)
    orthographic = segment.find(tag).text.lower()
    return remove_nonalpha(orthographic) 

def extract_interpretation(segment):
    interpretation = ".//{0}f[@name='interpretation']/{0}string".format(prefix)
    return segment.find(interpretation).text.lower()
    
def extract_gnc(interpretation):
    if len(interpretation) < 3:
        return interpretation[1]
    else:
        gender = next((token in interpretation if token in gender), None)
        number = next((token in interpretation if token in number), None)
        case = next((token in interpretation if token in case), None)
    return ''.join(filter(None, [gender, number, case]))

def split_interpretation(interpretation):
    interpretation = interpretation.split(':')
    base = interpretation[0]
    pos = interpretation[1]
    gnc = extract_gnc(interpretation)
    return base, pos, gnc

def append_orth(parsed, orth, pos): 
    if pos == 'aglt':
        parsed[-1] += pos
    elif pos not in ['brev', 'ign', 'interp', 'xxx']:
        parsed.append(pos)

def append_base(parsed, orth, base, pos): 
    if pos not in ['brev', 'ign', 'interp', 'xxx', 'aglt']:
        parsed.append(base)

def append_pos(orth, base, pos): 
    if pos not in ['brev', 'ign', 'interp', 'xxx']:
        parsed.append(pos)

def append_pos_gnc(orth, base, pos, gnc): 
    if pos not in ['brev', 'ign', 'interp', 'xxx']:
        parsed.append("{0}:{1}".format(pos, gnc))

def parse_sentence(sentence):
    parsed = []
    for segment in sentence.findall(segments):
        orth = extract_orthographic(segment)
        interp =  extract_interpretation(segment)
        base, pos, gnc = split_interpretation(interp)
        if is_num(orth):
            parsed.append('num')
        else:
            append_orth(parsed, orth, pos)
    return parsed

def parse(xmlpath, out):
    with open(out, 'a') as out:
        root = xml.etree.ElementTree.parse(filename).getroot()
        for sentence in root.findall(sentences):
            parsed = parse_sentence(sentence)
            if is_valid(parsed):
                parsed = contract_whitespace(' '.join(parsed))
                print(parsed, file=out)

if __name__ == '__main__':
    path = sys.argv[1]
    out= os.path.basename(os.path.normpath(path))
    open(out, 'w').close()
    xmlpath = os.path.join(path, '**/ann_morphosyntax.xml') 
    for filename in glob.iglob(xmlpath, recursive=True):
        try:
            parse(xmlpath, out)
        except Exception as err:
            print(err)
            continue
