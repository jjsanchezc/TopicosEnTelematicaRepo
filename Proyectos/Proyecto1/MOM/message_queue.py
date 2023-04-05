import json 

class MessageQueue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        self.dictionary = []
        self.dictionary={}

#Determina si las colas están vacias (False) o no (True)
    def is_empty(self):
        return not bool(self.dictionary)

#Agrega un nuevo elemento a la cola y al diccionario para asignarle un valor por mensaje
    def enqueue(self, message,topic_name):
<<<<<<< HEAD
        self.dictionary.append(message)
        self.save_to_file("message_queue.json")
        if message in self.dictionary:
=======
        self.topic_queue.append(message)
        
        if topic_name in self.dictionary:
>>>>>>> a40db5a989f6658af79f639b3390887359be4064
            self.dictionary[topic_name].append(message)
        else:
            self.dictionary[topic_name] = [message]
        self.save_to_file("message_queue.json")
        print(f"El mensaje: {message} ha sido agregado")

#elimina y devuelve con el pop el elemento de la cola
    def dequeue(self, message):
        return self.dictionary.pop(message)


#con el display se imprime la cola en consola
    def display(self):
        print(self.dictionary)

#metodo para recibir los mensajes de una cola
    def get_messages_from_topic(self,topic_name):
        with open('message_queue.json') as f:
            data = json.load(f)
        return data[topic_name]

#esto es para coger un mensaje en particular de la cola y enviarlo a un usuario
    def get_message(self, position):
        if position < 0 or position >= len(self.dictionary):
            raise IndexError("Index out of range")
        return self.dictionary[position]
    
#el usuario solicita el mensaje de la cola de su interes 
    def message_request(self, dictionary, position):
        if dictionary.is_empty():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        message = self.get_message(position)
        dictionary.dequeue(message)
        return message
    
#para términos de persistencia se guardarán los datos en un .json
    def save_to_file(self, queue_back):
        #se crea otro diccionario para guardar los datos que tiene la cola y el diccionario 
<<<<<<< HEAD
        queue_data = {'queues': self.dictionary, 'dictionary': self.dictionary}
=======
        queue_data = self.dictionary
>>>>>>> a40db5a989f6658af79f639b3390887359be4064
        with open(queue_back, 'w') as f:
            json.dump(queue_data, f,indent=4)
            print("Datos guardados en el archivo", queue_back)


#acá se carga al programa los datos que se habian guardado en el json
    def load_from_file(self, queue_back):
            with open(queue_back, 'r') as f:
                queue_data = json.load(f)
<<<<<<< HEAD
                self.dictionary = queue_data['queues']
=======
>>>>>>> a40db5a989f6658af79f639b3390887359be4064
                self.dictionary = queue_data['dictionary']
            print("Datos cargados del archivo", queue_back)

