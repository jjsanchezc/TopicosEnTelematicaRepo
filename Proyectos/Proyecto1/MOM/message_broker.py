from user import User

messages_queue = []
username='JJ'   

class MessageBroker:
    def __init__(self,topic_name,message):
        self.exchange=self.Exchange()
        self.message_queue=self.MessageQueue()
        self.topic_name=topic_name
        self.message=message
    
    class Exchange:
        
        #Methods for Topics
        def create_topic(self,name):
            pass
        
        def delete_topic(self,name):
            pass
        
        
        def publish_message(self,message,topic_name):
            '''send message to queue

            Args:
                message (str): message to send
                topic_name (str): topic name
            '''
        
        
    
    
    class Queue:
        '''la cola almacena y luego entrega los mensajes a cada consumir
        '''        
        def __init__(self) -> None:
            pass
        