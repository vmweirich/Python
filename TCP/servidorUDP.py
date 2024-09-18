import socket

#criando o socket
socketTCP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#realização do bind do processo na porta 2023
socketTCP.bind(("127.0.0.1",2023))
socketTCP.listen()
print("Servidor UDP está esperando conexões!")

#bloqueio da thread principal - esperando novas conexões
socketCliente, endereco = socketTCP.accept()
print(f"Endereco do cliente {endereco}")

#conexao feita, esperando requisicao do cliente 
msg = socketCliente.recv(1024)

#mensagem chegou!  vamos imprimir !
print(msg)

#enviando mensagem para o cliente 
socketCliente.sendall(str.encode("resposta do servidor!"))
socketCliente.close()