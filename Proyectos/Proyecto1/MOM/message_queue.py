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
        #print(f"El mensaje: {message} ha sido agregado..... {str(self.dictionary[0])}")
        self.save_to_file("MOM/message_queue.json")
        
        print(f"El mensaje: {message} ha sido agregado..... {str(self.dictionary[0])}")

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
    '''PAULI REVISA ESTO
    def get_message(self, position):
        if position < 0 or position >= len(self.topic_queue):
            raise IndexError("Index out of range")
        return self.topic_queue[position]
    '''
#el usuario solicita el mensaje de la cola de su interes 
    def message_request(self, dictionary, position):
        if dictionary.is_empty():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        #Revisa la lista 52
        #message = self.get_message(position)
        message='a'
        dictionary.dequeue(message)
        return message
    
#para términos de persistencia se guardarán los datos en un .json
    def save_to_file(self, queue_back):
        #se crea otro diccionario para guardar los datos que tiene la cola y el diccionario 
        queue_data = self.dictionary
        print(f'queue_data= {queue_data}')
        with open(queue_back, 'w') as f:
            json.dump(queue_data, f,indent=4)
            return print("Datos guardados en el archivo", queue_back)


#acá se carga al programa los datos que se habian guardado en el json
    def load_from_file(self, queue_back):
            with open(queue_back, 'r') as f:
                queue_data = json.load(f)
                self.dictionary = queue_data['queues']
                self.dictionary = queue_data['dictionary']
            print("Datos cargados del archivo", queue_back)

