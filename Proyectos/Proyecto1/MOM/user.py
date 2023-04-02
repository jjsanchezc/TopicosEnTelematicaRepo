from topics import Topics
from message_broker import MessageBroker
import json

class User:
    def __init__(self, username, password, role, publisher_topics=None, subscriber_topics=None):
        self.username = username
        self.password = password
        #se identifica si el rol es publicador o suscriptor o ambos
        self.role = role
        if role == 'publisher':
            self.publisher_topics = publisher_topics or []
            self.subscriber_topics = []
        elif role == 'subscriber':
            self.publisher_topics = []
            self.subscriber_topics = subscriber_topics or []
        elif role == 'publisher-subscriber':
            self.publisher_topics = publisher_topics or []
            self.subscriber_topics = subscriber_topics or []
        self.accounts_file_path = "accounts.json"

#Validacion del usuario
    def is_valid(self):
        with open(self.accounts_file_path, 'r') as f:
            data = json.load(f)
        if self.username in data and self.password == data[self.username][0]["password"]:
            return True
        else:
            return False

#registrar usuario en .json
    def register(self):
        with open(self.accounts_file_path, 'r') as f:
            data = json.load(f)
        new_user = {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "publisher_topics": self.publisher_topics,
            "subscriber_topics": self.subscriber_topics
        }
        data[self.username] = [new_user]
        with open(self.accounts_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return data


# First all the methods as a publisher
    def see_my_topics_pub(self):
        '''method used to see all my topics as a publisher

        Returns:
            list: returns in a list all my topics
        '''
        print(f'esta es la lista de topicos que tienes{self.publisher_topics}')
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

# Pregunta en consola al usuario los sig parametros 
username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter your role (publisher, subscriber, or publisher-suscriber): ")

if role == "publisher" or role == "publisher-suscriber":
    publisher_topics = input("Enter publisher topics (use comma): ").split(",")
else:
    publisher_topics = []

if role == "subscriber" or role == "publisher-suscriber":
    subscriber_topics = input("Enter subscriber topics (use comma): ").split(",")
else:
    subscriber_topics = []

# Crea un nuevo objeto de usuario y lo registra
user = User(username, password, role, publisher_topics, subscriber_topics)
accounts = user.register()

# verifica que el usuario si este en el archivo de accounts.json 
assert username in accounts
assert accounts[username][0]["password"] == password
assert accounts[username][0]["role"] == role
assert accounts[username][0]["publisher_topics"] == publisher_topics
assert accounts[username][0]["subscriber_topics"] == subscriber_topics

print("User registration test passed successfully!")


'''class User:
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
        return False'''
