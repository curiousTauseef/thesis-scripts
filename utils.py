gender_tags = {'m1', 'm2', 'm3', 'f', 'n'}
number_tags = {'pl', 'sg'}
case_tags = {'nom', 'gen', 'dat', 'acc', 'inst', 'loc', 'voc'}

def extract_gnc(interpretation):
    gender = next((token for token in interpretation if token in gender_tags), None)
    number = next((token for token in interpretation if token in number_tags), None)
    case = next((token for token in interpretation if token in case_tags), None)
    pos = interpretation[1]
    gnc = ''.join(list(filter(None, [gender, number, case])))
    if gnc:
        return "{0}:{1}".format(pos, gnc)
    return pos

def split_interpretation(interpretation):
    interpretation = interpretation.split(':')
    base = interpretation[0]
    pos = interpretation[1]
    gnc = extract_gnc(interpretation)
    return base, pos, gnc

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
