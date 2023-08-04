from flask import Flask, jsonify, render_template, session, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from http import HTTPStatus
from mate import generate_kiste, MateKiste
from chat import Chat
import bson.json_util as json_util


app = Flask(__name__,
            template_folder='templates',
            static_folder='static',)
app.secret_key = 'super secret key 1234 5678 9012 3456 '
socketio = SocketIO(app)

clients = []

STANDARD_ROOM = 0

@app.route('/', methods=['GET'])
def index():
    response = jsonify(success=True)
    response.status_code = HTTPStatus.MOVED_PERMANENTLY
    if session.get('logged_in'):
        return redirect('/session')
    else:
        return redirect('/login')
    raise NotImplementedError()

@app.route('/login', methods=['GET'])
def login():
    response = jsonify(success=True)
    response.status_code = 200
    return render_template('login.html')

@app.route('/session', methods=['GET'])
def omg_i_hate_copilot_session():
    response = jsonify(success=True)
    response.status_code = 200
    return render_template('session.html')

@app.route('/api', methods=['GET'])
def api():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/login', methods=['GET'])
def api_login():
    session['logged_in'] = True
    response = jsonify(success=True)
    response.status_code = HTTPStatus.MOVED_PERMANENTLY
    return redirect('/session')


@app.route('/api/mate', methods=['GET'])
def api_mate():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/mate/status', methods=['GET'])
def api_mate_status():
    FLASCHE_COUNT = 20
    response = jsonify(kiste=MateKiste.getStatus())
    response.status_code = 200
    return response

@app.route('/api/chat/', methods=['GET'])
def api_chat():
    messages = Chat.getNextNMessages(100, 0) # 0 offset
    response = jsonify(success=True, messages=json_util.dumps(messages)) 
    response.status_code = 200 
    return response

@socketio.on('chat-message')
def handle_chat_message(data):
    print(data)
    Chat.insertMessage(data['text'], data['sender'], data['timestamp'])

@socketio.on('chat-get-messages')
def handle_chat_get_message(data):
    messages = Chat.getNextNMessages(data['count'], data['skip'])
    # dont fucking touch this
    data = { 'messages': json_util.dumps(messages) }
    return { 'data': data }

@socketio.on('mate-status')
def handle_mate_status():
    status = MateKiste.getStatus()
    return { 'data':  status }

@socketio.on('mate-nehmen')
def handle_mate_nehmen(data):
    MateKiste.removeAt(data['row'], data['column'])
    emit('mate-genommen', data, broadcast=True)

@socketio.on('mate-reset')
def handle_mate_reset():
    MateKiste.reset()
    emit('mate-resetten', broadcast=True)


@socketio.on('connect')
def handle_connect():
    join_room(STANDARD_ROOM)

@socketio.on('disconnect')
def handle_disconnect():
    leave_room(STANDARD_ROOM)

@app.route('/api/music', methods=['GET'])
def api_music():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/music/skip', methods=['POST'])
def api_music_skip():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/music/queue', methods=['GET'])
def api_music_queue():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/music/add_song', methods=['POST'])
def api_music_add_song():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.errorhandler(404)
def page_not_found(error):
    response = jsonify(success=False)
    response.status_code = 404
    return render_template('404.html'), response

if __name__ == '__main__':
    Chat.init()
    MateKiste.init()
    socketio.run(app, debug=True, host='localhost', port=5000) #pragma: no cover
