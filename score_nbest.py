import argparse
from srilm import LM

def get_score_function(lm):
    def score_function(hypothesis):
        return lm.total_logprob_strings(hypothesis.strip().split())
    return score_function

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lm', help='path to the language model file', type=str)
    parser.add_argument('out', help='path to the output file', type=str)
    parser.add_argument('nbest', help='path to the nbest list file', type=str)
    args = parser.parse_args()
    lm = LM(args.lm.encode('utf-8'))
    score = get_score_function(lm)
    with open(args.nbest, 'r') as f, open(args.out, 'w') as out:
        for line in f:
            index, text = line.strip().split("\t")
            out.write("{}\n".format(score(text)))
