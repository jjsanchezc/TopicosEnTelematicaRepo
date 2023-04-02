from user import User
from message_queue import MessageQueue
from exchange import Exchange

messages_queue = []
username='JJ'   

class MessageBroker:
    def __init__(self,topic_name,message):
        #self.exchange=Exchange()
        self.message_queue=MessageQueue()
        self.topic_name=topic_name
        self.message=message
