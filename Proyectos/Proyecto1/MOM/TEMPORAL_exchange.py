from topics import Topics
from queue import MessageQueue
class Exchange:
    def __init__(self,publisher_topic_list,subscriber_topic_list,topic_name):
        self.pub_topic_list=publisher_topic_list
        self.sub_topic_list=subscriber_topic_list
        self.topic_name=topic_name
        self.topics=Topics()
        self.message_queue=MessageQueue()

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
        self.topics.add_message(message)