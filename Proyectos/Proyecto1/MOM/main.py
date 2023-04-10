from flask import Flask, render_template, request, redirect, jsonify, session
import json
from user import User
from message_broker import MessageBroker
from exchange import Exchange

app = Flask(__name__)
app.secret_key = b'secret_key'
message_broker = ''
# exchange=''
# username=''


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def home_login():
    global message_broker, exchange, username
    '''home page, where the user will log in

    Returns:
        returns the "page" where the user will select if they want to be publisher or subscriber
    '''
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']
    # Validate the user's credentials
    # user=User(username,password)
    user = User(username, password, role)
    if user.is_valid():
        publisher_topics, subscriber_topics = get_topics(username)
        session['username'] = username
        session['role'] = user.role
        message_broker = MessageBroker(publisher_topics, subscriber_topics)
        exchange = Exchange(publisher_topics, subscriber_topics)

        return redirect("/menu")
    else:
        return jsonify({"mensaje": 'Credenciales incorrectas'})
    '''if user.is_valid():
        jsonify({"mensaje":'cuenta valida'})
        return redirect("/menu")
    return jsonify({"mensaje":'incorrecto'})'''

# hay que editar este ya que en user.py ya se decide el rol


@app.route('/menu', methods=['GET'])
def menu():
    if 'username' in session:
        # ya entró ahora debe aparecer el menu del rol segun si es publicador o suscriptor o ambos
        return 'Hola, decide que quieres ser'
    else:
        return redirect('/login')


'''    return 'hola, decide que quieres ser'''


@app.route('/menu', methods=['POST'])
def menu_choice():
    choice = session.get['role']
    print(choice)
    if choice == "publisher":
        return redirect("/menu/publisher")
    # crear subscriber menu y para ambos
    elif choice == 'subscriber':
        # go to subscriber
        return redirect("/menu/publisher")
    elif choice == 'publisher-subscriber':
        # go to both
        return redirect("/menu/publisher")
    else:
        return redirect("/menu")

# PUBLISHER


@app.route('/menu/publisher', methods=['GET'])
def menu_publisher():
    return jsonify({"mensaje": 'hola, decide que quieres hacer',
                    "opcion 1": "ver mis topicos",
                    "opcion 2": "añadir topicos",
                    "opcion 3": "eliminar topicos",
                    "opcion 4": "Enviar topicos"})


@app.route('/menu/publisher', methods=['POST'])
def menu_publisher_choice():
    choice = request
    if choice == '1':
        # go to publisher
        pass
    elif choice == '2':
        # go to subscriber
        pass
    else:
        return redirect("/menu")


@app.route('/menu/publisher/topics/add_topic/', methods=['POST'])
def add_topic():

    # cambiamos esto por un json?
    # PRUEBA
    username = "JJ"
    publisher_topics, subscriber_topics = get_topics(username)
    exchange = Exchange(publisher_topics, subscriber_topics)

    topic_name = request.json["topic_name"]
    if exchange.create_topic(username, topic_name):
        exchange.get_name_pub_topic_list()
        return jsonify({"message": "topico creado con exito"})
    exchange.get_name_pub_topic_list()
    return jsonify({'message': 'error al crear el topico'})


@app.route('/menu/publisher/topics', methods=['GET'])
def see_topics():
    return exchange.get_name_pub_topic_list()


@app.route('/menu/publisher/message/<topic_name>', methods=['POST'])
def send_message(topic_name):
    # PRUEBA
    username = "JJ"
    publisher_topics, subscriber_topics = get_topics(username)
    exchange = Exchange(publisher_topics, subscriber_topics)

    message = input('mensaje a mandar: ')
    try:
        exchange.publish_message(message, topic_name)
        return jsonify({"mensaje": "mensaje enviado correctamente"})
    except:
        return jsonify({"mensaje": "error en el mensaje"})
    '''if user.send_message(topic_name) is False:
        return jsonify({'mensaje': 'Error al enviar, topico no existe','a': str(user.my_topics_pub)})
    else:
        message=request.json['mensaje']
        add_queue(message)
        
        return jsonify({'mensaje': 'Mensaje enviado correctamente para los subscriptores de '+topic_name})'''


# Ruta para recibir un mensaje
@app.route('/mensaje', methods=['GET'])
def recibir_mensaje():
    # PRUEBA
    username = "jjs"
    publisher_topics, subscriber_topics = get_topics(username)
    exchange = Exchange(publisher_topics, subscriber_topics)
    print(exchange.get_name_sub_topic_list())
    topic_name = input('de cual topico quieres buscar mensajes')
    exchange.get_messages(topic_name)


def get_topics(username):
    f = open("MOM/accounts.json", "r")
    data = json.loads(f.read())
    publisher_topics_list = data[username][0]["publisher_topics"]
    subscriber_topics_list = data[username][0]["subscriber_topics"]
    return publisher_topics_list, subscriber_topics_list


if __name__ == '__main__':
    app.run(debug=False)
