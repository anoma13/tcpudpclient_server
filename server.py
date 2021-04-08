from threading import Thread
import time
import socket
from socket import * 

msg_listUDP = ['','waiting...(ketikkan sesuatu untuk mendapat pesan)']
msg_listTCP = ['','waiting...(ketikkan sesuatu untuk mendapat pesan)']

def UDPListen():
    clientUDP = ("127.0.0.1", 12345)
    s = socket(AF_INET, SOCK_DGRAM) 
    s.bind((clientUDP))
    while True:
        msg, add = s.recvfrom(2048)
        print(" Message Client UDP :", msg, "From :", add)
        tp = str(msg)
        msg_listUDP.append(tp)
        reply = msg_listTCP[-1]
        msg_client = str.encode(reply)
        s.sendto(msg_client, add) 

def TCPListen():
    clientTCP = ("127.0.0.1", 12346)
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((clientTCP))
    while True:
        s.listen(1)
        conn, add = s.accept()
        msg = conn.recv(1024)
        print (" Message Client TCP :", msg, "From :", add)
        tp = str(msg)
        msg_listTCP.append(tp)
        reply = msg_listUDP[-1]
        msg_client = str.encode(reply)
        conn.send(msg_client)
        conn.close()

def main():
    ThreadUDP = Thread(target=UDPListen)
    ThreadTCP = Thread(target=TCPListen)

    print ("Loading...")
    ThreadUDP.start()
    ThreadTCP.start()
    print ("Enjoy Chatting!!!")

if __name__ == "__main__":
    main()