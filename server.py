import socket

# create socket
s = socket.socket()

# bind to localhost and port 5000
host = 'localhost'
port = 5000
s.bind((host, port))

# start listening on this socket
s.listen(5)
print('listening for incoming connections')

# accept a connection
c, addr = s.accept()
print('connected to client')

# receive messages
c.recv(32)
c.recv(1024)
c.recv(32)
