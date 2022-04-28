import socket
s = socket.socket()
s.connect(("localhost",4000))
msg = s.recv(1024) # 1024 is buffer size --> no. of bytes recieved at a time
while msg:
    print("Received:",msg.decode())
    msg = s.recv(1024) #looping as long as message comes in

s.close()
