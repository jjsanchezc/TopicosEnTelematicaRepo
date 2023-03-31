from topics import Topics
from message_broker import MessageBroker
import json

class User:
    def __init__(self, username,password=None):
        self.user = username
        self.password=password
        f=open("MOM/accounts.json","r")
        self.data=json.loads(f.read())
        self.my_topics_pub = self.data[self.user][0]["pusbliser_topics"]
        self.my_topics_sub = self.data[self.user][0]["subscriber_topics"]
        self.message_broker=MessageBroker(self.my_topics_pub,self.my_topics_sub)
    
    
    def is_valid(self):
        #por ahora dejar esta implementacion sencilla de usuario
        try:
            self.data=self.data[self.user]
        except:
            return False
        if self.password == self.data[0]["password"]:
            return True
        return False


# First all the methods as a publisher
    def see_my_topics_pub(self):
        '''method used to see all my topics as a publisher

        Returns:
            list: returns in a list all my topics
        '''
        print(f'esta es la lista de topicos que tienes{self.my_topics_pub}')
        return self.my_topics_pub

    def add_topic_pub(self, topic_name)-> bool:
        '''method used to create a topic a topic, it will be stored in a list

        Args:
            name (string): name of the topic the user wants to create
        '''
        name=self.user+'_'+topic_name
        topic=Topics(topic_name)
        #añadir el codigo para modificar el .json
        if name in self.my_topics_pub:
            print('no se ha podido crear el topico porque ya existe uno con ese nombre')
            return False
        else:
            self.my_topics_pub.append(name)
            print('topic agregado')
            return True

    def rm_topic_pub(self, name):
        if not name in self.my_topics_pub:
            return print('no se ha podido eliminar el topico porque no existe un topico con ese nombre')
        else:
            self.my_topics_pub.pop(name)
            return print('topic borrado')

    def send_message(self, topic_name) -> bool:
        if topic_name in self.my_topics_pub:
            return True
        else:
            return False
