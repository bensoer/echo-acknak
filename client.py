__author__ = 'bensoer'

from socket import *
import sys


class Client:



    def __init__(self):
        self.__clientSocket = socket(AF_INET, SOCK_DGRAM)
        #self.__serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.__clientSocket.bind(('localhost', 7000))
        self.__buffer = 2048
        self.__lockCycle = False

    def lockCycles(self):
        self.__lockCycle = True

    def checkWithServer(self, portNumber, ip, message):
        print("Checking with The Server")


        self.__clientSocket.sendto(message.encode(), (ip, portNumber))

        print("Sent - Waiting on Response")
        response, serverAddress = self.__clientSocket.recvfrom(self.__buffer)
        print("Response Arrived")
        print(response)

        if(self.__lockCycle):
            self.__keepChecking(portNumber, ip)

    def __keepChecking(self, portNumber, ip):

            print("Enter Another Valid IP and Port Pair to Test Against the Server")
            message = input()
            self.checkWithServer(portNumber, ip, message)





