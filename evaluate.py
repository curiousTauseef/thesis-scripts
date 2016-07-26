import distance
import operator
import argparse
from collections import defaultdict
from srilm import LM

def read_nbest_list(filename):
    nbest = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            index, text = line.split("\t")
            nbest[int(index)].append(text)
    return nbest

def get_prob_fun(lm):
    def calculate_prob(hypothesis):
        return lm.total_logprob_strings([word.encode('utf-8') for word in hypothesis.split()])
    return calculate_prob

def calculate_werr(reference, hypothesis):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to the language model file', type=str)
    parser.add_argument('test', help='path to the test file', type=str)
    args = parser.parse_args()
    lm = LM(args.path.encode('utf-8'))
    score = get_prob_fun(lm)
    nbest = read_nbest_list(args.test)
    werr_total = 0
    for index in nbest:
        reference = nbest[index][0]
        hypotheses = nbest[index][1:]
        scores = [(hypothesis, score(hypothesis)) for hypothesis in hypotheses] 
        best = max(scores, key=operator.itemgetter(1))
        distance = distance.levenshtein(reference.split(), best.split()) 
        werr_total +=  distance/len(reference)
    print(werr_total/len(hypo))
