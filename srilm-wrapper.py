from srilm import LM
import argparse

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('path_to_lm', help='path to the language model file', type=str)
    #args = parser.parse_args()
    lm = LM('./text_plain_full_novocab.lm')
    with open('sentences') as sentences:
        for line in sentences:
            print("{0}: {1}".format(line.strip(), lm.total_logprob_strings(line.split())))
