import argparse

tags = ['subst', 'depr', 'num', 'numcol', 'adj',
        'adja', 'adjp', 'adjc', 'adv', 'ppron12',
        'ppron3', 'siebie', 'fin', 'bedzie', 'aglt',
        'praet', 'impt', 'imps', 'inf', 'pcon', 'pant',
        'ger', 'pact', 'ppas', 'winien', 'pred', 'prep',
        'conj', 'comp', 'qub', 'brev', 'burk', 'interj']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()
    with open(args.input, 'r') as f, open(args.input + '_filtered', 'w') as out:
        for line in f:
            print(' '.join(word for word in line.split() if word.split(':')[0] in tags), file=out)
