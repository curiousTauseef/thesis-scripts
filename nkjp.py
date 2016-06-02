#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import re
import string

prefix = '{http://www.tei-c.org/ns/1.0}'
sentences = ".//{0}s".format(prefix)
segments = ".//{0}seg".format(prefix)

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
    
def extract_gnc(tags):
    gender = ['m1', 'm2', 'm3', 'f', 'n']
    number = ['sg', 'pl']
    case = ['nom', 'gen', 'dat', 'acc', 'inst', 'loc', 'voc']
    
def parse_sentence(sentence):
    parsed = []
    for segment in sentence.findall(segments):
        orth = extract_orthographic(segment)
        interp =  extract_interpretation(segment).split(':')
        base, pos = interp[0], interp[1]
        if is_num(orth):
            parsed.append('num')
        elif pos == 'aglt':
            parsed[-1] += orth
        elif pos not in ['brev', 'ign', 'interp', 'xxx']:
            parsed.append(orth)
    return parsed

def parse(filename, out):
    with open(out, 'a') as out:
        root = xml.etree.ElementTree.parse(filename).getroot()
        for sentence in root.findall(sentences):
            parsed = parse_sentence(sentence)
            if is_valid(parsed):
                parsed = contract_whitespace(' '.join(parsed))
                print(parsed, file=out)

if __name__ == '__main__':
    path = '/media/sebastian/Seagate Expansion Drive/mgr/nkjp/misc/ustawy'
    pattern = os.path.join(path, '/**/ann_morphosyntax.xml') 
    for filename in glob.iglob(pattern, recursive=True):
        try:
            parse(filename, out)
        except Exception as err:
            print(err)
            continue
