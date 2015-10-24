__author__ = 'bensoer'

from socket import *
'''
SocketSystem is a general class for creating and managing udp sockets. It is intended to be inherited from
by the client or server wishing to make socket connections
'''
class SocketSystem:

    def __init__(self):
        self.__socketSystem = socket(AF_INET, SOCK_DGRAM)
        self.__buffer = 2048

    '''
    bindSocket binds the passed address and port number to the socket
    :param address: the address to bind to
    :param port: the port to bind to
    '''
    def bindSocket(self, address, port):
        self.__socketSystem.bind((address, port))

    '''
    setBuffer sets the buffer size for recieving messages. By default it is set to 2048 at initialization
    :param buffer : the buffer size to be set
    '''
    def setBuffer(self, buffer):
        self.__buffer = buffer

    '''
    receiveMessage recieves a message from the socket.
    '''
    def recieveMessage(self):
        return self.__socketSystem.recvfrom(self.__buffer)

    '''
    sendMessage sewnds a message over the established socket
    :param message: the message to be sent over the socket
    :param clientAddress: the tuple of the address to send the message to
    '''
    def sendMessage(self, message, clientAddress=0):
        self.__socketSystem.sendto(message, clientAddress)

    '''
    closeSocketConnection closes the socket when the transaction has completed
    '''
    def closeSocketConnection(self):
        self.__socketSystem.close()

    '''
    createNewSocket creates a new socket
    '''
    def createNewSocket(self):
        self.closeSocketConnection()
        self.__socketSystem = socket(AF_INET, SOCK_DGRAM)