import json 

class MessageQueue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        self.dictionary={}

#Determina si las colas están vacias (False) o no (True)
    def is_empty(self):
        return not bool(self.dictionary)

#Agrega un nuevo elemento al diccionario para asignarle un valor por mensaje
    def enqueue(self, message, topic_name):
        if message in self.dictionary:
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

#metodo para recibir los mensajes de un diccionario en general
    def get_messages_from_topic(self,topic_name):
        with open('message_queue.json') as f:
            data = json.load(f)
        return data[topic_name]


#el usuario solicita el mensaje del diccionario en la posición 0 de la llave de cada usuario
    def message_request(self, dictionary):
        if dictionary.is_empty():
            return "La cola está vacía"
        with open('message_queue.json') as f:
            data = json.load(f)
#cambiar por el nombre del tópico
            message= data.get(dictionary.message_queue[0], '')
        dictionary.dequeue(message)
        self.save_to_file('queue_back.json')
        return message
    
#para términos de persistencia se guardarán los datos en un .json
    def save_to_file(self, queue_back):
        with open(queue_back, 'w') as f:
            json.dump(self.dictionary, f,indent=4)
            print("Datos guardados en el archivo", queue_back)


#acá se carga al programa los datos que se habian guardado en el json
    def load_from_file(self, queue_back):
            with open(queue_back, 'r') as f:
                self.dictionary= json.load(f)
            print("Datos cargados del archivo", queue_back)

