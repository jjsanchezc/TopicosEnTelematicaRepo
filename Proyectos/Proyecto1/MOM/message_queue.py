import json 

class MessageQueue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        with open('MOM/message_queue.json') as f:
            data = json.load(f)
        self.dictionary=data

#Determina si las colas están vacias (False) o no (True)
    def is_empty(self):
        return not bool(self.dictionary)

#Agrega un nuevo elemento a la cola y al diccionario para asignarle un valor por mensaje
    def enqueue(self, message,topic_name):
        #buscar otro metodo para agregar en un diccionario
        #self.dictionary.append(message)
        print(f'queue, este es el mensaje que recibi {message} y lo guardo en {topic_name}')
        if topic_name in self.dictionary:
            self.dictionary[topic_name].append(message)
        else:
            self.dictionary[topic_name]=[message]
        self.save_to_file("MOM/message_queue.json")
        
        print(f"El mensaje: {message} ha sido agregado..... {str(self.dictionary[0])}")

#elimina y devuelve con el pop el elemento de la cola
    def dequeue(self, message):
        return self.dictionary.pop(message)


#con el display se imprime la cola en consola
    def display(self):
        print(self.dictionary)

#metodo para recibir los mensajes de un diccionario en general
    def get_messages_from_topic(self,topic_name):
        with open('MOM/message_queue.json') as f:
            data = json.load(f)
        try:
            return data[topic_name]
        except:
            return "No eres subscriptor o no existe el topico"


#el usuario solicita el mensaje del diccionario en la posición 0 de la llave de cada usuario
    def message_request(self, dictionary):
        if dictionary.is_empty():
            return "La cola está vacía"
        with open('MOM/message_queue.json') as f:
            data = json.load(f)
#cambiar por el nombre del tópico
            message= data.get(dictionary.message_queue[0], '')
        dictionary.dequeue(message)
        self.save_to_file('MOM/message_queue.json')
        return message
    
#para términos de persistencia se guardarán los datos en un .json
<<<<<<< HEAD
    def save_to_file(self, queue_back):
        #se crea otro diccionario para guardar los datos que tiene la cola y el diccionario 
        queue_data = {'queues': self.dictionary, 'dictionary': self.dictionary}
        with open(queue_back, 'w') as f:
            json.dump(queue_data, f,indent=4)
            print("Datos guardados en el archivo", queue_back)
=======
    def save_to_file(self):
        #se crea otro diccionario para guardar los datos que tiene la cola y el diccionario 
        with open('MOM/message_queue.json', 'w') as f:
            data = json.load(f)
            json.dump(data, f,indent=4)
            print("Datos guardados en el archivo")
>>>>>>> 8ea5a579b54c86d2c3feb1dbb7617c110acd85d8


#acá se carga al programa los datos que se habian guardado en el json
    def load_from_file(self):
            with open('MOM/message_queue.json', 'r') as f:
                self.dictionary= json.load(f)
            print("Datos cargados del archivo")

