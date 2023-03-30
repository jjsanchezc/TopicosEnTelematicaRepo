import socket
import requests

def send_message(message):
    
    # Creamos un socket y nos conectamos al servidor MOM
    user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user_socket.connect(('localhost', 8000))

    # Enviamos el mensaje al servidor MOM
    user_socket.sendall(message.encode())

    # Cerramos la conexión
    user_socket.close()

if __name__ == '__main__':
    # Enviamos un mensaje de prueba al servidor MOM
    send_message('Hola, mundo!')
