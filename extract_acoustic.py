#requires Python >= 3.5
import argparse
import glob
import itertools
import os

def group_lines(lines):
    return [list(group) for key, group in itertools.groupby(lines, lambda x: not x.startswith('HYPOTHESIS')) if key]

def sum_group(group):
    return sum([float(line.strip().split(',')[1]) for line in group])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the corpus folde', type=str)
    parser.add_argument('output', help='path to the output file', type=str)
    args = parser.parse_args()
    subdirectories = sorted([subdir[0] for subdir in os.walk(args.input)][1:]) 
    for index, folder in enumerate(subdirectories):
        filename = os.path.join(folder, 'acoustic_hypotheses.csv')
        with open(filename, 'r') as f, open(args.output, 'a') as out:
            out.write(filename + '\n')
            grouped = group_lines(f.readlines())
            for group in grouped:
                print([float(line.strip().split(',')[1]) for line in group])
                print(sum_group(group))
                out.write("{}\n".format(sum_group(group)))
