from socket import *
import ssl
import threading

def handle_client(connectionSocket, addr):
    print(addr[0])

    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


serverPort = 7000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='C:/certificates/certificate.pem', keyfile='C:/certificates/key.pem', password="1234")

serverSocket = socket(AF_INET, SOCK_STREAM, 0)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
secureSocket = context.wrap_socket(serverSocket, server_side=True)
print("Server is ready")
while True:
    connectionSocket, addr = secureSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()
