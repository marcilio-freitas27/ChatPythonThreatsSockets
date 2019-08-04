# chat server tcp
import socket

# criação do socket
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

# associação
sock_server.bind((host, port))
sock_server.listen(5)

print('PyChat - Aguardando usuários')

# conexão dos clients

c = 0
usuarios = []
nomes = []
while c < 2: # a quantidade de clientes é determinada aqui(c < clientes)
	b, addr2 = sock_server.accept()
	nome = b.recv(1024)
	print('{} entrou. {}'.format(nome.decode('ascii'),str(addr2)))
	c+=1
	usuarios.append(b)
	nomes.append(nome.decode('ascii')) # apenas um teste

print('Bem vindos! Vamos PyChatear B)')
# troca de mensagens(recebimento e envio)
msg2 = ''
while msg2 != 'q' :
	for a in usuarios:
		msg2 = a.recv(1024)
		if msg2 == 'q':
			b.close()
			break
			print('PyChat - Aguardando usuários')
		else:
			print("{}".format(msg2.decode('ascii')))
			for i in usuarios:
					i.send(msg2)
