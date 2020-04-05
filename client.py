import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

x = input("Enter your message.")
s.send(bytes("Chatting with RamsayBot", "utf-8"))

full_msg=''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)


#This is to be used by the 'other' chatbot to chat with RamsayBot. 
#The address 1234 must not be changed. 
