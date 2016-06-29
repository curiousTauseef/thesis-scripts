from srilm import LM
import argparse

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('path_to_lm', help='path to the language model file', type=str)
    #args = parser.parse_args()
    lm = LM('./data/text_plain_full.lm')
    with open('test_tiny_hypotheses') as sentences:
        for line in sentences:
            print("{0}: {1}".format(line.strip(), lm.total_logprob_strings(line.split())))
