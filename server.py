__author__ = 'bensoer'

from socket import *

'''
Server defines all the functionality for the server in the echo-acknak demo project. It created a UDP socket which
it listens for requests, checking incoming ones if they are searching for valid IP and port numbers in thier payload
and then returns an ACK or NAK deoending if they are valid. It also sends a UDP hello message on ACK to the specified
IP and port in the payload
'''
class Server:

    def __init__(self):
        self.__validServers = ["127.0.0.1:8888"]

        self.__serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.__serverSocket.bind(('localhost', 8000))
        self.__buffer = 2048

    '''
    startListening starts the server to listen onto the port and be ready to process incoming requests
    '''
    def startListening(self):
        self.__printStatus("Server Is Now Actively Listening For Requests")

        while True:
            message, clientAddress = self.__serverSocket.recvfrom(self.__buffer)
            message = message.decode()
            print("Server Recieved A Message: " + message)
            print("Checking if It Is Valid")

            if(self.__checkIsValid(message)):
                self.__sendResponse("ACK", clientAddress)

                #send hello to the passed message
                parts = message.split(":")
                self.__sendHello(parts[1], parts[0])
            else:
                self.__sendResponse("NAK", clientAddress)

    '''
    sendResponse sends a response back to the calling client depending on whether it is an ACK or NAK response needed
    :param type: the type of response to be returned. Valid values are 'ACK' and 'NAK'
    :param clientAddress: the client address object from recieving the UDP request
    '''
    def __sendResponse(self,type, clientAddress):
        if(type == "ACK"):
            print("It Is Valid. Sending Back ACK")
            self.__serverSocket.sendto("ACK".encode(), clientAddress)
        elif(type == "NAK"):
            print("It Is Invalid. Sending Back NAK")
            self.__serverSocket.sendto("NAK".encode(), clientAddress)

    def __sendHello(self, port, ip):
        self.__serverSocket.sendto("Hello!".encode(), (ip, int(port)))


    '''
    printStatus is a private helper method that prints a statusMessage to the console
    :param statusMessage: the message to be printed to the screen
    '''
    def __printStatus(self, statusMessage):
        print(statusMessage)

    '''
    checkIsValid is a private helper method that checks if the payload address is a valid address. A valid address is
    determined by whether or not the address matches an address stored in the server 'validAddress' array
    :param socketAddress: the address passed in the payload of the UDP request
    '''
    def __checkIsValid(self,socketAddress):
        servers = self.getValidServers()

        for server in servers:
            if(server == socketAddress):
                return True

        return False

    '''
    getValidServers returns the list of valid servers
    '''
    def getValidServers(self):
        return self.__validServers

    '''
    setValidServers sets the valid servers array with the passed in array
    :param validServers: an array of validServers used to determine if a client request is valid
    '''
    def setValidServers(self, validServers):
        self.__validServers = validServers

    '''
    removeValidServer removes the address passed in the parameter from the validServers array
    :param validServer: the address to be removed from the validServer array
    '''
    def removeValidServer(self, validServer):
        for index in range(len(self.__validServers)):
            if(self.__validServers[index] == validServer):
                del(self.__validServers[index])
                break

    '''
    addValidServer adds the address passed in the parameter to the validServers array
    :param validServer: the address to be added to the validServer array
    '''
    def addValidServer(self, validServer):
        self.__validServers.append([validServer])

'''
Initialization code for the server so that a seperate file does not need to be created in this example
'''
server = Server()
server.startListening()