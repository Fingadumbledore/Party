from flask import Flask, jsonify, render_template, session, redirect
from http import HTTPStatus

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',)
app.secret_key = 'super secret key 1234 5678 9012 3456 '

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
def session():
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
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/mate/trinken', methods=['POST'])
def api_mate_trinken():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/chat/', methods=['GET'])
def api_chat():
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/chat/messages/<count>', methods=['GET'])
def api_chat_messages_1(count):
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/chat/messages/<count>/<offset>', methods=['GET'])
def api_chat_messages_2(count, offset):
    response = jsonify(success=True)
    response.status_code = 200
    return response

@app.route('/api/chat/new_message', methods=['POST'])
def api_chat_new_message():
    response = jsonify(success=True)
    response.status_code = 200
    return response

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

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000) #pragma: no cover

