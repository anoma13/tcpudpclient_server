from socket import *
serverTCP = ("127.0.0.1", 12346)
while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(serverTCP)
    message = input("Client TCP :")
    msgToserver = str.encode(message)
    s.send(msgToserver)
    msg = s.recv(1024)
    print("Client UDP :",msg)