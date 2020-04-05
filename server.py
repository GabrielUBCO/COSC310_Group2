import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Welcome to RamsayBot", "utf-8"))
    clientsocket.close()
    
#This is to be used to communicate with another bot using the '1234' as the address. 
#This code can be added to the RamsayBot.py when we wish to make it chat with another bot. 

#Unfortunately, we could not test our implementation since we were unable to contact any other group willing to work on it. 
#We added the code here, in case we could be graded partially.
