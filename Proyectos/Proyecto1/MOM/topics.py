class Topics:
    def __init__(self,name=None):
        self.name=name
    
    def set_topic(self,name):
        self.name=name
    
    def get_name(self):
        print(f'este es el nombre del topico {self.name}')
        return str(self.name)
    def message(self):
        print('envio el mensaje del topico')
        return str(f'mensaje para todos los subscriptores de {self.name}')