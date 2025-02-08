from socket import *


IP="localhost"
PORT=50000


s=socket(AF_INET, SOCK_STREAM)



try:
    s.connect((IP,PORT))
    print("Start connecting with server...")
    print("waiting for a response")
    
    msg_server=s.recv(1024).decode()
    
    print("Server > " + msg_server)
    
    print("Write a message for the server")
    while True:
        msg=input()
        s.send(msg.encode())
        print("Message sent!")
        
        
except:
    print("There is no client")
    



s.close()
