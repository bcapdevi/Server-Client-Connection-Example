from socket import *

#getting name of host
serverName = gethostname()
#declaring port
serverPort = 12000

#Initializing and connecting socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#Prompting user to input sentence to be converted
sentence = input('Input lowercase sentence: ')
#Sending the sentence to server
clientSocket.send(sentence.encode())

#receiving response from server
modifiedSentence = clientSocket.recv(1024)
#printing response from server
print('From Server', modifiedSentence.decode())

#closing connection
clientSocket.close()