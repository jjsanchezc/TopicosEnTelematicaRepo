class Exchange:
    def __init__(self,name):
        self.name=name
    
    def set_name(self,name):
        '''setter del nombre del exchange
        Args:
            name (_type_): _description_
        '''   
        self.name=name
    def binding(self):
        '''las reglas de enrutamiento que se utilizan para enviar los mensajes entrantes a las colas
        de mensajes adecuadas. Cada binding está asociado con una clave de enrutamiento,
        que se utiliza para determinar a qué colas de mensajes se deben enviar los mensajes entrantes.
        Las claves de enrutamiento son expresiones de tema que describen el patrón de coincidencia de temas que se utiliza para enrutar los mensajes a las colas de mensajes adecuadas. 
        '''   
        pass
    def routing_key(self):
        pass