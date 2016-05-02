import concraft
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('output', help='path to the output file', type=str)
    parser.add_argument('-t', '--tokens', help='type of the output tokens, use p for POS tags and l for lemmas (default)', type=str, choices='pl', default='l')
    args = parser.parse_args()
    server = concraft.Server()
    client = concraft.Client(server.get_port())
    mapping = {'l': client.to_lemmas, 'p': client.to_pos_tags}
    with open(args.input, 'r') as infile, open(args.output, 'w') as out:
        for line in infile:
            print(line)
            out.write(mapping[args.tokens](line))
