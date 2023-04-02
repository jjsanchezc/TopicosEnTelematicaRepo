from flask import Flask, jsonify, redirect, request, session
from user import User
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

messages_queue = []

#MENU INICIAL

@app.route('/login', methods=['POST'])
def home_login():
    '''home page, where the user will log in

    Returns:
        returns the "page" where the user will select if they want to be publisher or subscriber
    '''  
    username=request.json['username']
    password=request.json['password']
    # Validate the user's credentials
    user=User(username,password)
    if user.is_valid():
        session['username'] = username
        session['role'] = user.role
        return redirect("/menu")
    else:
        return jsonify({"mensaje": 'Credenciales incorrectas'})
    '''if user.is_valid():
        jsonify({"mensaje":'cuenta valida'})
        return redirect("/menu")
    return jsonify({"mensaje":'incorrecto'})'''


#hay que editar este ya que en user.py ya se decide el rol
@app.route('/menu', methods=['GET'])
def menu():
    '''if 'username' in session:
        return 'Hola, decide que quieres ser'
    else:
        return redirect('/login')'''
    return 'hola, decide que quieres ser'

@app.route('/menu', methods=['POST'])
def menu_choice():
    choice=request.json["role"]
    print(choice)
    if choice=="publisher":
        return redirect("/menu/publisher")
    #crear subscriber menu y para ambos
    elif choice=='subscriber':
        #go to subscriber
        return redirect("/menu/publisher")
    elif choice=='publisher-subscriber':
        #go to both
        return redirect("/menu/publisher")
    else:
        return redirect("/menu")

#PUBLISHER
@app.route('/menu/publisher', methods=['GET'])
def menu_publisher():
    return jsonify({"mensaje":'hola, decide que quieres ser',
                    "opcion 1":"ver mis topicos",
                    "opcion 2":"añadir topicos",
                    "opcion 3":"eliminar topicos",
                    "opcion 4":"Enviar topicos"})
@app.route('/menu/publisher', methods=['POST'])
def menu_publisher_choice():
    choice=request
    if choice=='1':
        #go to publisher
        pass
    elif choice=='2':
        #go to subscriber
        pass
    else:
        return redirect("/menu")

@app.route('/menu/publisher/topics/add_topic/', methods=['POST'])
def add_topic():
    topic_name=request.json['topic_name']
    if user.add_topic_pub(topic_name):
        user.see_my_topics_pub()
        return jsonify({"message":"topico creado con exito"})
    user.see_my_topics_pub()
    return jsonify({'message':'error al crear el topico'})

@app.route('/menu/publisher/topics', methods=['GET'])
def see_topics():
    return user.see_my_topics_pub()


@app.route('/menu/publisher/message/<topic_name>', methods=['POST'])
def send_message(topic_name):
    if user.send_message(topic_name) is False:
        return jsonify({'mensaje': 'Error al enviar, topico no existe','a': str(user.my_topics_pub)})
    else:
        message=request.json['mensaje']
        add_queue(message)
        
        return jsonify({'mensaje': 'Mensaje enviado correctamente para los subscriptores de '+topic_name})



#despues va a pasar a la clase de message_broker
def add_queue(mensaje):
    messages_queue.append(mensaje)




user=User("JJ")

# Ruta para recibir un mensaje
@app.route('/mensaje', methods=['GET'])
def recibir_mensaje():
    if len(messages_queue) == 0:
        return jsonify({'mensaje': 'No hay mensajes'})
    else:
        mensaje = messages_queue.pop(0)
        return jsonify({'mensaje': mensaje})






if __name__ == '__main__':
    app.run(debug=True)
