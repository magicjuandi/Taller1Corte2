import socket
import threading

def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                clients.remove(client_socket)
                client_socket.close()
                break
            for client in clients:
                if client != client_socket:
                    client.send(message.encode("utf-8"))
        except:
            break
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(5)

    print("[*] Servidor de mensajería iniciado en localhost:9999")

    clients = []

    while True:
        client_socket, _ = server.accept()
        print("[*] Cliente conectado:", client_socket)

        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_thread.start()

if __name__ == "__main__":
    main()
