import json 

class MessageQueue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        self.topic_queue = []
        self.dictionary={}

#Determina si las colas están vacias (False) o no (True)
    def is_empty(self):
        return not bool(self.topic_queue)

#Agrega un nuevo elemento a la cola y al diccionario para asignarle un valor por mensaje
    def enqueue(self, message,topic_name,queue_back):
        self.topic_queue.append(message)
        self.save_to_file(queue_back)
        if message in self.dictionary:
            self.dictionary[topic_name].append(message)
        else:
            self.dictionary[topic_name] = [message]
        print(f"El mensaje {message} ha sido agregado")

#elimina y devuelve con el pop el elemento de la cola
    def dequeue(self, message):
        return self.topic_queue.pop(message)


#con el display se imprime la cola en consola
    def display(self):
        print(self.topic_queue)

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
    
#para términos de persistencia se guardarán los datos en un .json
    def save_to_file(self, queue_back):
        #se crea otro diccionario para guardar los datos que tiene la cola y el diccionario 
        queue_data = {'queues': self.topic_queue, 'dictionary': self.dictionary}
        with open(queue_back, 'w') as f:
            json.dump(queue_data, f)
            print("Datos guardados en el archivo", queue_back)


#acá se carga al programa los datos que se habian guardado en el json
    def load_from_file(self, queue_back):
            with open(queue_back, 'r') as f:
                queue_data = json.load(f)
                self.topic_queue = queue_data['queues']
                self.dictionary = queue_data['dictionary']
            print("Datos cargados del archivo", queue_back)

