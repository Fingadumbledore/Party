import os
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Verzeichnis zum Speichern der hochgeladenen Bilder
UPLOAD_FOLDER = 'upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# SQLite-Datenbank initialisieren
DATABASE = 'session.db'

def create_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Tabelle "session" erstellen, wenn sie nicht existiert
    c.execute('''CREATE TABLE IF NOT EXISTS session
                 (name TEXT, number INTEGER, file1 TEXT, file2 TEXT, checkbox2 INTEGER, input2 TEXT, checkbox3 INTEGER)''')

    conn.commit()
    conn.close()

create_database()

@app.route('/get_create_session', methods=['POST'])
def get_create_session():
    print(request.form)
    name = request.form['name']
    number = request.form['number']
    checkbox2 = 1 if 'checkbox2' in request.form else 0
    input2 = request.form['input2']
    checkbox3 = 1 if 'checkbox3' in request.form else 0

    file1 = None
    file2 = None
    file1_path = None
    file2_path = None

    # Überprüfen, ob Datei1 hochgeladen wurde
    if 'file1' in request.files:
        file1 = request.files['file1']
        if file1.filename != '':
            file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
            file1.save(file1_path)

    # Überprüfen, ob Datei2 hochgeladen wurde
    if 'file2' in request.files:
        file2 = request.files['file2']
        if file2.filename != '':
            file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
            file2.save(file2_path)

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Daten in die "session"-Tabelle einfügen
    c.execute("INSERT INTO session (name, number, file1, file2, checkbox2, input2, checkbox3) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, number, file1_path, file2_path, checkbox2, input2, checkbox3))

    conn.commit()
    conn.close()

    return 'Session erfolgreich erstellt!'

if __name__ == '__main__':
    app.run()
