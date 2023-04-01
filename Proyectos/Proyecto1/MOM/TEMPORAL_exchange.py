from topics import Topics
from queue import Queue
class Exchange:
    def __init__(self,publisher_topic_list,subscriber_topic_list):
        self.pub_topic_list=publisher_topic_list
        self.sub_topic_list=subscriber_topic_list
        self.topics=Topics()
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
        