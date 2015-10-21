__author__ = 'bensoer'

from client import Client

while True:

    print("Enter A Valid IP To Check With The Server")
    message = input()
    client = Client()
    client.sendRequest(8000,'localhost', message)
    client.closeConnection()