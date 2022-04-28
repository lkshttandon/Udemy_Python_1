import socket

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #InternetProtocolV4,type of conn = TCPIP ,default values
s.bind((host,port))
s.listen(1) # no of connection to connect
print("Server listening on port:",port)
c,address = s.accept() #return conn obj and connection of client

filename = c.recv(1024)
try:
    f = open(filename,'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"File does not exist")
c.close()