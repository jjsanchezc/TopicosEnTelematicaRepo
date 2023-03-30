import socket

def receive_messages(message=None):
    # Creamos un socket y nos conectamos al servidor MOM
    user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user_socket.connect(('localhost', 8000))

    # Recibimos los mensajes enviados a través del servidor MOM
    if not message:
        while True:
            data = user_socket.recv(1024)
            if not data:
                break
            print('Mensaje recibido:', data.decode())
    else:
        user_socket.sendall(message.encode())

    # Cerramos la conexión
    user_socket.close()

if __name__ == '__main__':
    # Recibimos los mensajes enviados a través del servidor MOM
    receive_messages()
