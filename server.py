from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xx11xx'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('chat.msg', namespace='/chat')
def test_message(message):
    print("Message received:{}".format(message['data']))
    emit('chat.echo', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/chat')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, port=8181, debug=True)
