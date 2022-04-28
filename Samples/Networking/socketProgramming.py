import socket

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #InternetProtocolV4,type of conn = TCPIP ,default values
s.bind((host,port))
s.listen(1) # no of connection to connect
print("Server listening on port:",port)
c,address = s.accept() #return conn obj and connection of client
print("Connection from:",str(address))
c.send(b"Hello, How are you?") # encoded to binary to send
# c.send("bye".encode()) alternate for encoding
c.close()