__author__ = 'bensoer'

from client import Client

message = "127.0.0.1:8888"
client = Client()
client.lockCycles()
client.checkWithServer(8000,'localhost', message)