class Queue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        self.topic_queue = Queue()


#Determina si las colas están vacias (False) o no (True)
    def is_empty(self):
        return not bool(self.topic_queue)


#Agrega un nuevo elemento a la cola
    def enqueue(self, message, times):
        self.topic_queue.append(message)
        print(f"El elemento {message} ha sido agregado {times} veces a la cola.")


#elimina y devuelve con el pop el elemento de la cola
    def dequeue(self, message):
        return self.topic_queue.pop(message)


#con el display se imprime la cola en consola
    def display(self):
        print(self.topic_queue)


#Agregar un mensaje a la cola especificada 
    def queue_add(self, message, times):
        for i in range(times):
            self.topic_queue.enqueue(message)


#esto es para coger un mensaje en particular de la cola y enviarlo a un usuario
    def get_message(self, position):
        if position < 0 or position >= len(self.topic_queue):
            raise IndexError("Index out of range")
        return self.topic_queue[position]
    
#el usuario solicita el mensaje de la cola de su interes 
    def message_request(self, topic_queue, position):
        if topic_queue.is_empty():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        message = self.get_message(position)
        topic_queue.dequeue(message)
        return message


