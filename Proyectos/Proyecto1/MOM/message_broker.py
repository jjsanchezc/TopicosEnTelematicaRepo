from user import User

messages_queue = []
username='JJ'   

class MessageBroker:
    def __init__(self,topic_name,message):
        self.exchange=self.Exchange()
        self.queue=self.Queue()
        self.topic_name=topic_name
        self.message=message
    
    class Exchange:
        def __init__(self) -> None:
            pass
        
        #Publisher
        def get_topics_pub(self):
            pass
        
        def send_message(self,message):
            pass
        
        def add_topic(self,topic_name):
            pass
        
        def delete_topic(self,topic_name):
            pass
        
        
    
    
    class Queue:
        '''la cola almacena y luego entrega los mensajes a cada consumir
        '''        
        def __init__(self) -> None:
            pass
        