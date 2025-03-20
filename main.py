from flask import Flask, render_template
from flask_socketio import SocketIO, send

# criar app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['DEBUG'] = True  # Habilitar modo de depuração

#criar funcao de enviar msg
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# criar primeira rota(pagina)
@app.route("/")
def homepage():
    return render_template('homepage.html')

# rodar o nosso app
# if __name__ == "__main__":
#     app.run(debug=True)

#roda o nosso app
socketio.run(app, host=" 192.168.0.105")



#pip install python-socketio flask-socketio simple-websocket