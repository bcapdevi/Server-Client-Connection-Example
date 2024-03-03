from socket import *

#declaring port
serverPort = 12000

#initializing socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#assigning host to port
serverSocket.bind(('x-10-5-50-72.wifi.stedwards.edu', serverPort))

#server listening for request
serverSocket.listen(1)

print('The server is ready to receive')


#Infinite loop waiting to receivw request and when recieved, put in upper case
while True:

    #Waiting for connection with client
    connectionSocket, addr = serverSocket.accept()

    #decoding recieved sentence
    sentence = connectionSocket.recv(1024).decode()
    #converting the sentence to upper case
    capitalizedSentence = sentence.upper()

    #sending the sentence back to client
    connectionSocket.send(capitalizedSentence.encode())

    #closing the connection
    connectionSocket.close()