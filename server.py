__author__ = 'bensoer'

from socket import *
class Server:

    def __init__(self):
        self.__validServers = ["127.0.0.1:8888"]

        self.__serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.__serverSocket.bind(('localhost', 8000))
        self.__buffer = 2048

    def startListening(self):
        print("Server Is Now Actively Listening For Requests")

        while True:
            message, clientAddress = self.__serverSocket.recvfrom(self.__buffer)
            message = message.decode()
            print("Server Recieved A Message: " + message)
            print("Checking if It Is Valid")

            if(self.__isValid(message)):
                print("It Is Valid. Sending Back ACK")
                self.__serverSocket.sendto("ACK".encode(), clientAddress)
            else:
                print("It Is Invalid. Sending Back NAK")
                self.__serverSocket.sendto("NAK".encode(), clientAddress)


    def __isValid(self,socketAddress):
        servers = self.getValidServers()

        for server in servers:
            if(server == socketAddress):
                return True

        return False

    def getValidServers(self):
        return self.__validServers

    def setValidServers(self, validServers):
        self.__validServers = validServers

    def removeValidServer(self, validServer):
        for index in range(len(self.__validServers)):
            if(self.__validServers[index] == validServer):
                del(self.__validServers[index])
                break;

    def addValidServer(self, validServer):
        self.__validServers.appen([validServer])


server = Server()
server.startListening()