import socket
import time
from socket_functions import Socket_function





class User(Socket_function):
    def __init__(self):
        s = socket.socket()
        s.connect(('127.0.0.1', 5005))
        port = int(self.empfangeStr(s))
        print(port)
        time.sleep(0.1)
        self.komm_s = socket.socket()
        self.komm_s.connect(('172.16.0.36', port))
        print(self.empfangeStr(self.komm_s))
        self.name = input()
        self.sendeStr(self.komm_s,self.name)
        while True:
            self.sendeStr(self.komm_s,input("input:"))




user1 = User()