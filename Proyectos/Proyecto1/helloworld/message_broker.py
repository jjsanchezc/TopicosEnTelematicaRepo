import socket
import threading
import queue

class MessageBroker:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', port))
        self.socket.listen()

        self.connections = []

        self.message_queue = queue.Queue()

        # Iniciamos un hilo para procesar la cola de mensajes
        threading.Thread(target=self.process_messages).start()

    def run(self):
        print('Message broker is running...')

        while True:
            # Esperamos por una conexión entrante
            user_socket, address = self.socket.accept()

            # Agregamos la conexión a la lista de conexiones
            print('recibi una conexión nueva')
            self.connections.append(user_socket)

            # Iniciamos un hilo para manejar la conexión del usere
            threading.Thread(target=self.handle_connection, args=(user_socket,)).start()

    def handle_connection(self, user_socket):
        while True:
            # Leemos los datos recibidos del usere
            data = user_socket.recv(1024)

            # Si no hay datos, cerramos la conexión
            if not data:
                self.connections.remove(user_socket)
                user_socket.close()
                break

            # Agregamos los datos a la cola de mensajes
            self.message_queue.put(data)

    def process_messages(self):
        while True:
            # Obtenemos el siguiente mensaje de la cola
            message = self.message_queue.get()
            for connection in self.connections:
                #print(f'he enviado todos los mensajes y esta son las conexiones {self.connections}')
                connection.sendall(message)

if __name__ == '__main__':
    # Creamos una instancia del broker de mensajes y lo iniciamos
    message_broker = MessageBroker(8000)
    message_broker.run()