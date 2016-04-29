import os
import re
import socket
import subprocess
from retry import retry
from collections import OrderedDict

PATH_TO_CONCRAFT = '~/.cabal/bin'

class Server:
    def __init__(self):
        self.port = self.find_free_port()
        self.server = self.start_server()

    def __del__(self):
        self.server.terminate()

    def find_free_port(self):
        sock = socket.socket()
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        return port

    def start_server(self):
        command = "{0}/concraft-pl server {0}/model.gz --port {1}".format(PATH_TO_CONCRAFT, self.port)
        server = subprocess.Popen(command, shell=True)
        return server
        
    def get_port(self):
        return self.port

class Client:
    def __init__(self, port):
        self.port = port

    @retry(subprocess.CalledProcessError, delay=10)
    def call_concraft(self, sentence):
        self.write_to_file(sentence)
        command = "{0}/concraft-pl client --port {1} < input".format(PATH_TO_CONCRAFT, self.port)
        return subprocess.check_output(command, shell=True).decode('utf-8')

    def to_lemma(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return [value[1] for key, value in parsed.items()]

    def to_pos(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return [value[0] for key, value in parsed.items()]

    def parse(self, concraft_output):
        parsed = OrderedDict()
        for line in concraft_output.split('\n'):
            if not line:
                continue
            elif not line.startswith('\t'):
                word = line.split()[0]
            elif line.split()[-1] == 'disamb':
                parsed[word] = (line.split()[0].lower(), line.split()[1])
        return parsed
    
    def write_to_file(self, sentence):
        with open('input', 'w') as input:
            input.write(sentence)

    def extract_lemmas(self, concraftOutput):
        return [line.split()[0] for line in concraftOutput.split("\n") if self.disambiguation(line)]

    def extract_pos(self, concraftOutput):
        return [line.split()[1] for line in concraftOutput.split("\n") if self.disambiguation(line)]

    def disambiguation(self, line):
        return line and line.split()[-1] == 'disamb'
