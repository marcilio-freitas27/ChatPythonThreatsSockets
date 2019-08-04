# chat client tcp
import socket
from threading import Thread

# criação da classe filha de Thread
class Chat(Thread):
        def __init__(self, name):
                Thread.__init__(self)
                self.name = name
        #inicio do socket
        def run(self):
                sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostname()
                port = 12345

                # conexão
                sock_client.connect((host, port))
                sock_client.send(self.name.encode('ascii'))

                # envio das mensagens
                print(self.name)
                msg = input('-->')
                while msg != 'q':
                        sock_client.send('\n'.encode('ascii') + self.name.encode('ascii') +' : '.encode('ascii')+msg.encode('ascii') +'\n'.encode('ascii'))
                        # envio do nome e msg do cliente

                        dados = sock_client.recv(1024)
                        print("{}".format(dados.decode('ascii')))

                        print(self.name)
                        msg = input('-->') # depois da primeira msg, pressione enter para ver se tem alguma recebida.
                sock_client.close()     # Obs: as mensagens dos usuários 2 em diante só são vistas/enviadas com enter em cada usuário a partir da primeira msg.
                                                        # Obs2: O primeiro usuário também fica nesse tipo de visualização/recebimento após o 1º envio

Chat(input('Digite o seu nome: ')).start()
