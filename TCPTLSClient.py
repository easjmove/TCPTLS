from socket import *
import ssl

server_address = 'localhost'
server_name = 'server'
serverPort = 7000

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

socket = create_connection((server_address, serverPort))
secureSocket = context.wrap_socket(socket, server_hostname=server_name)

sentence = input('Input sentence: ')
secureSocket.send(sentence.encode())
modifiedSentence = secureSocket.recv(1024).decode()
print('From server: ', modifiedSentence)
secureSocket.close()
