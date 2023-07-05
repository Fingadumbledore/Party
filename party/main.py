#from party import app
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    @app.route('/', methods=['GET'])
    def index():
        response = jsonify(success=True)
        response.status_code = 200
        return response

    @app.route('/api', methods=['GET'])
    def api():
        response = jsonify(success=True)
        response.status_code = 200
        return response

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

    return app

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
