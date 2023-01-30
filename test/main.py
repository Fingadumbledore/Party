from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
  file = request.files['file']
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
  return 'Datei hochgeladen'

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
  app.run()
