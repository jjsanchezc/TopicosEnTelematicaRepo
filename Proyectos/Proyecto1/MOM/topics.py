from queue import MessageQueue
class Topics:
    def __init__(self,name=None):
        self.name=name
        self.message_queue=MessageQueue()
    
    def set_topic(self,name):
        self.name=name
    
    def get_name(self):
        print(f'este es el nombre del topico {self.name}')
        return str(self.name)
    def add_message(self,message):
        print('envio el mensaje del topico')
        self.message_queue.enqueue(message)
        return str(f'mensaje para todos los subscriptores de {self.name}')