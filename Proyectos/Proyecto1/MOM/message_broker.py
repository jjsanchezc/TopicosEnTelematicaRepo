from user import User
from message_queue import MessageQueue
from exchange import Exchange

messages_queue = []
username='JJ'   

class MessageBroker:
    def __init__(self,publisher_topic_list,subscriber_topic_list):
        exchange=Exchange(publisher_topic_list,subscriber_topic_list)
        self.message_queue=MessageQueue()