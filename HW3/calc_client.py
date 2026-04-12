import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))

while True:
    num = input('calc num: ')

    if num == 'q':
        s.send(num.encode())
        break

    s.send(num.encode())
    data = s.recv(1024).decode()

    print('result calc: ', data)

s.close()