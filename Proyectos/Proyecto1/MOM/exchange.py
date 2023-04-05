import json
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
        with open('accounts.json') as f:
            data = json.load(f)
        
        name=username+"_"+topic_name
        new_topic=Topics(name)
        
        if name in self.pub_topic_name_list:
            #no se hace nada porque ya existe
            return False
        self.pub_topic_name_list.append(name)
        data[username][0]["publisher_topics"].append(new_topic)
        with open('accounts.json', 'w') as f:
            json.dump(data, f)
        return True
    
    def delete_topic(self,username,name)->bool:
        with open('accounts.json') as f:
            data = json.load(f)
        if name in self.pub_topic_name_list:
            #abrir el json y sobreescribir
            data[username][0]["publisher_topics"].remove(name)
            with open('accounts.json', 'w') as f:
                json.dump(data, f)
            return True
        #topico no existe
        return False
    
    
    #METHODS FOR PUBLISHERS
    def publish_message(self,message,topic_name):
        '''send message to queue

        Args:
            message (str): message to send
            topic_name (str): topic name
        '''
        self.topics.add_message(message,topic_name)
        
    #METHODS FOR SUBSCRIBERS
    def get_messages(self,topic_name):
        return self.topics.message_queue.get_messages_from_topic(topic_name)