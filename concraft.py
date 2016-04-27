import os
import re
import socket
import subprocess
import time
import wdnet
from retrying import retry

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
        call = "{0}/concraft-pl server {0}/model.gz --port {1}".format(PATH_TO_CONCRAFT, self.port)
        server = subprocess.Popen(call, shell=True)
        return server
        
    def get_port(self):
        return self.port

class Client:
    def __init__(self, port):
        self.port = port

    @retry(wait_fixed = 10000)
    def __call__(self, sentence):
        call = "{0}/concraft-pl client --port {1} < input".format(PATH_TO_CONCRAFT, self.port)
        self.write_to_file(sentence)
        return subprocess.check_output(call, shell=True).decode('utf-8')

    def to_lemmas(self, sentence):
        return get_lemmas(self, self.__call__(sentence))

    def to_pos(self, sentence):
        return get_lemmas(self, self.__call__(sentence))

    def write_to_file(self, sentence):
        with open('input', 'w') as input:
            input.write(sentence)

    def extract_lemmas(self, concraftOutput):
        return [line.split()[0] for line in concraftOutput.split("\n") if self.disambiguation(line)]

    def extract_pos(self, concraftOutput):
        return [line.split()[1] for line in concraftOutput.split("\n") if self.disambiguation(line)]

    def disambiguation(self, line):
        return line and line.split()[-1] == 'disamb'
