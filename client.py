import socket

s=socket.socket()

s.connect(("192.168.58.1",52320))
print (s.recv(1024))
