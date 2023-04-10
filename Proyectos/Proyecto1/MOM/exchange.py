import json
from topics import Topics
from message_queue import MessageQueue
class Exchange:
    def __init__(self,publisher_topic_list=None,subscriber_topic_list=None):
        self.pub_topic_list=publisher_topic_list
        self.pub_topic_name_list=self.get_name_pub_topic_list()
        self.sub_topic_list=subscriber_topic_list
        self.sub_topic_name_list=self.get_name_sub_topic_list()
        self.topics=Topics()
        self.message_queue=MessageQueue()



    #METHODS FOR PUBLISHERS
    def get_name_pub_topic_list(self):
        name_list=[]
        #for topic in self.pub_topic_list():
        for topic in self.pub_topic_list:
            #name_list.append(topic.get_name())
            name_list.append(topic)
        return name_list
    
    def create_topic(self,username,topic_name):
        with open('MOM/accounts.json') as f:
            data = json.load(f)
        
        name=username+"_"+topic_name
        new_topic=Topics(name)
        
        if name in self.pub_topic_name_list:
            #no se hace nada porque ya existe
            return False
        self.pub_topic_name_list.append(name)
        #data[username][0]["publisher_topics"].append(new_topic)
        data[username][0]["publisher_topics"].append(name)
        with open('MOM/accounts.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    
    def delete_topic(self,username,name)->bool:
        with open('MOM/accounts.json') as f:
            data = json.load(f)
        if name in self.pub_topic_name_list:
            #abrir el json y sobreescribir
            data[username][0]["publisher_topics"].remove(name)
            #erase topic from each subscriber
            for user_list in data.values():
                for user in user_list:
                    if name in user["subscriber_topics"]:
                        user["subscriber_topics"].remove(name)
            with open('MOM/accounts.json', 'w') as f:
                json.dump(data, f,indent=4)
            return True
        #topico no existe
        return False
    
    
    
    def publish_message(self,message,topic_name):
        '''send message to queue

        Args:
            message (str): message to send
            topic_name (str): topic name
        '''
        self.topics.add_message(message,topic_name)
        
    #METHODS FOR SUBSCRIBERS
    def get_name_sub_topic_list(self):
        name_list=[]
        #for topic in self.sub_topic_list():
        for topic in self.sub_topic_list:
            #name_list.append(topic.get_name())
            name_list.append(topic)
        return name_list
    
    def get_messages(self,topic_name):
        return self.topics.message_queue.get_messages_from_topic(topic_name)
    
    def subscribe(self,username,name):
        available_topics=[]
        with open('MOM/accounts.json') as f:
            data = json.load(f)
        #check if the user is already a subscriber
        if name not in self.sub_topic_name_list:
            data[username][0]["subscriber_topics"].append(name)
        else:
            return 'no te puedes suscribir dos veces al mismo topico'
        for user_list in data.values():
            for user in user_list:
                if user["publisher_topics"]!= []:
                    available_topics.append(user["publisher_topics"])
        print(f'topicos disponibles {available_topics}')
        with open('MOM/accounts.json', 'w') as f:
            json.dump(data, f,indent=4)
        return 'te has suscrito al topico correctamente'
    
    def unsubscribe(self,username,name):
        with open('MOM/accounts.json') as f:
                data = json.load(f)
        #check if the user is already a subscriber
        if name in self.sub_topic_name_list:
            data[username][0]["subscriber_topics"].remove(name)
        else:
            return 'no te puedes cancelar la suscripcion de un topico al cual no estas suscrito'
        with open('MOM/accounts.json', 'w') as f:
            json.dump(data, f,indent=4)
        return f'has cancelado la suscripcion de {name}'