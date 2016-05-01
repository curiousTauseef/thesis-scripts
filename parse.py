import concraft
import argparse

parser = argparse.ArgumentParser()
args = parser.add_argument("input", help="path to the input file", type=str)
args = parser.add_argument("output", help="path to the output file", type=str)
parser.parse_args()
server = concraft.Server()
port = server.get_port()
client = concraft.Client(port)

print(client.to_lemma(sentence))
print(client.to_pos(sentence))
