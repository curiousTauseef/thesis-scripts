#requires Python >= 3.5
import argparse
import glob
import os
import yaml
from natsort import natsorted

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the corpus folde', type=str)
    parser.add_argument('output', help='path to the output file', type=str)
    args = parser.parse_args()
    with open(os.path.join(args.input, 'metadata.yml'), 'r') as metadata:
            references = [elem[':answer'] for elem in yaml.load(metadata)]
    subdirectories = natsorted([subdir[0] for subdir in os.walk(args.input)][1:]) 
    for index, folder in enumerate(subdirectories):
        filename = os.path.join(folder, 'acoustic_hypotheses.txt')
        print(filename)
        with open(filename, 'r') as f, open(args.output, 'a') as out:
            out.write("{0} {1}\n".format(index+1, references[index]))
            for line in f:
                line = line.split()[1:-1]
                out.write("{0} {1}\n".format(index+1, ' '.join(line)))
