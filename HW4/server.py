import socket
import os

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)
    
    print("응답 대기 중")

    while True:
        client_socket, addr = server_socket.accept()
        try:
            request = client_socket.recv(1024).decode()
            if not request:
                client_socket.close()
                continue

            filename = request.split('\n')[0].split()[1]
            if filename == '/':
                filename = '/index.html'
            filepath = filename.lstrip('/')

            if os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    content = f.read()
                
                response_header = "HTTP/1.1 200 OK\r\n"
                if filepath.endswith(".html"):
                    response_header += "Content-Type: text/html; charset=utf-8\r\n"
                elif filepath.endswith(".png"):
                    response_header += "Content-Type: image/png\r\n"
                
                response_header += f"Content-Length: {len(content)}\r\n\r\n"
                
                client_socket.send(response_header.encode())
                client_socket.send(content)
            else:
                header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
                body = "<html><body><h1>Not Found</h1></body></html>"
                client_socket.send(header.encode() + body.encode())
        except Exception:
            pass
        finally:
            client_socket.close()

if __name__ == "__main__":
    run_server()