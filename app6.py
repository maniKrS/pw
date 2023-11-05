from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chatbot.html')

@socketio.on('chat message')
def handle_message(message):
    emit('chat message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
