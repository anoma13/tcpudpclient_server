from socket import *
serverUDP = ("127.0.0.1", 12345)
while True:
    s = socket(AF_INET, SOCK_DGRAM)
    message = input("Client UDP :")
    msgToserver = str.encode(message)
    s.sendto(msgToserver, (serverUDP))
    msg, add = s.recvfrom(1000)
    print("Client TCP :",msg)