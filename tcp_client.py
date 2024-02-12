import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.18.70.232', 12345))
s.send(b'Dan & Shilo')

# data = s.recv(100)
# print("Server sent: ", data)

s.send(b'208968560 & 318469830')

s.close()