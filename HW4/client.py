import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('127.0.0.1', 8080))
        request = "GET /index.html HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
        client_socket.send(request.encode())

        response = client_socket.recv(4096).decode(errors='ignore')
        status_line = response.split('\r\n')[0]
        print(status_line)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()