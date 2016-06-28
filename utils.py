import re

gender_tags = {'m1', 'm2', 'm3', 'f', 'n'}
number_tags = {'pl', 'sg'}
case_tags = {'nom', 'gen', 'dat', 'acc', 'inst', 'loc', 'voc'}

def write_hypotheses(filename, hypo):
    with open(filename + '_hypotheses', 'w') as out:
        for index in sorted(hypo):
            for line in hypo[index]:
                out.write("{0} {1}".format(index, line))

def read_hypotheses(filename):
    hypo = defaultdict(list)
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            hypo[index+1].append(line)
    return hypo

def read_unigrams(filename):
    with open(filename, 'r') as f:
        unigrams = [line.split()[0] for line in f]
    return unigrams

def extract_gnc(interpretation):
    gender = next((token for token in interpretation if token in gender_tags), None)
    number = next((token for token in interpretation if token in number_tags), None)
    case = next((token for token in interpretation if token in case_tags), None)
    pos = interpretation[0]
    gnc = ''.join(list(filter(None, [gender, number, case])))
    if gnc:
        return "{0}:{1}".format(pos, gnc)
    return pos

def split_interpretation(interpretation):
    interpretation = interpretation.split(':')
    base = interpretation[0]
    pos = interpretation[1]
    gnc = extract_gnc(interpretation[1:])
    return base, pos, gnc

def remove_nonalpha(string):
    pattern = re.compile('[\W_]+', re.UNICODE)
    return pattern.sub('', string)

def contract_whitespace(string):
    pattern = re.compile('\s+')
    return pattern.sub(' ', string)

def is_num(orth):
    roman = ['ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    return orth in roman or any(char.isdigit() for char in orth)

def is_valid(line):
    return len(line) > 4 and line.count('num') < 3
