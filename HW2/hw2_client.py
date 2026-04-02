import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

name = 'Jisoo Lee'
sock.send(name.encode())


data = sock.recv(4)
id = int.from_bytes(data, 'big')
print(id)
