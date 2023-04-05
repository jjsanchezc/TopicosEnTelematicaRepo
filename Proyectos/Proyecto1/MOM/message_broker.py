from user import User
from message_queue import MessageQueue
from exchange import Exchange

messages_queue = []
username='JJ'   

class MessageBroker:
    def __init__(self,topic_name,message,publisher_topic_list,subscriber_topic_list):
        super().__init__(publisher_topic_list,subscriber_topic_list,topic_name)
        self.message_queue=MessageQueue()
        self.topic_name=topic_name
        self.message=message
