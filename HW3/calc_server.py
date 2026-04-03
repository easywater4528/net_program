import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(5)

while True:
    client, addr = s.accept()
    print('Connected from ', addr)

    while True:
        data = client.recv(1024)

        if not data:
            break

        msg = data.decode() 

        try:
            data = eval(msg)
            if '/' in msg: 
                result = f"{data:.1f}"
            else:
                result = str(int(data))

            client.send(result.encode())

        except:
            client.send(b'Try again')

        

    client.close()