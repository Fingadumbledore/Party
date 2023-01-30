from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():

    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return jsonify({'message': 'File uploaded successfully'})

@app.route('/download')
def download_file():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'download.txt', as_attachment=True)

if __name__ == '__main__':
    app.run()
