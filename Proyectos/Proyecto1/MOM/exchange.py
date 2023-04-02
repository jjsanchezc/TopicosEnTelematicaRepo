from topics import Topics
from message_queue import MessageQueue
class Exchange:
    def __init__(self,publisher_topic_list,subscriber_topic_list,topic_name):
        self.pub_topic_list=publisher_topic_list
        self.pub_topic_name_list=self.get_name_pub_topic_list()
        self.sub_topic_name_list=subscriber_topic_list
        self.topic_name=topic_name
        self.topics=Topics()
        self.message_queue=MessageQueue()



    #Methods for Topics
    def get_name_pub_topic_list(self):
        name_list=[]
        for topic in self.pub_topic_list:
            name_list.append(topic.get_name())
        return name_list
    
    def create_topic(self,username,topic_name):
        name=username+"_"+topic_name
        Topics(name)
        self.pub_topic_name_list.append(name)
        if name in self.pub_topic_name_list:
            #no se hace nada porque ya existe
            return False
        #deberia sobreescribir el json
        return True
    
    def delete_topic(self,name):
        if name in self.pub_topic_name_list:
            #abrir el json y sobreescribir
            pass
        else:
            #topico no existe
            pass
    
    
    def publish_message(self,message,topic_name):
        '''send message to queue

        Args:
            message (str): message to send
            topic_name (str): topic name
        '''
        self.topics.add_message(message,topic_name)