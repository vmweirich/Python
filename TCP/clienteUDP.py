import socket

#criando socket UDP
socketUDP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#enviando requisições para o servidor
socketTCP.connect(("127.0.0.1",2023))

#lendo respostas do servidor
resposta = socketUDP.recvfrom(1024)

#imprimindo mensagem do servidor na tela
msg = "mensagem do servidor {}".format(resposta[0])
print(msg) 

