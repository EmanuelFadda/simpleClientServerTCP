from socket import *

s=socket(AF_INET, SOCK_STREAM)

port=50000

s.bind(("",port))

s.listen(1)

while True:
    c,add=s.accept()
    print(add)
    
    c.send("Welcome!".encode())
    
    while True:
        msg_client=c.recv(1024).decode()
        print("Client > "+msg_client)
    
