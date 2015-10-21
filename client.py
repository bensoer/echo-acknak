__author__ = 'bensoer'

from socket import *

'''
Client defines the client functions for the echo-acknak demo system
'''
class Client:

    def __init__(self):
        self.__clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.__clientSocket.bind(('localhost', 7000))
        self.__buffer = 2048


    '''
    sendRequest sends a UDP request using a parameter passed port, ip and message for payload. The message is sent
    and then a recieve is awaited upon and decoded before the function returns
    :param portNumber: the port to send the request to
    :param ip: the ip to send the request to
    :param message: the message being sent in the request
    '''
    def sendRequest(self, portNumber, ip, message):
        print("Checking with The Server")

        self.__clientSocket.sendto(message.encode(), (ip, portNumber))
        print("Sent - Waiting on Response")

        response, serverAddress = self.__clientSocket.recvfrom(self.__buffer)
        print("Response Arrived")
        print(response.decode())

    '''
    closeConnextion closes the UDP connection so that the port can be released and renewed for the next connection
    request
    '''
    def closeConnection(self):
        self.__clientSocket.close()



