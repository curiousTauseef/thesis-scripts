import concraft

server = concraft.Server()
port = server.get_port()
client = concraft.Client(port)

sentence = "pchnąć w tę Łódź jeża Wałbrzych Lub ośm skrzyń fig"
client.to_lemma(sentence)
#print(client.to_lemma(sentence))
#print(client.to_pos(sentence))
