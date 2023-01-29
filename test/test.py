from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('chat.db', check_same_thread=False)
cursor = conn.cursor()

# Tabelle erstellen, falls sie nicht existiert
cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                   (id INTEGER PRIMARY KEY, username TEXT, message TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/enter_chat", methods=["GET", "POST"])
def enter_chat():
    if request.method == "POST":
        # Handle POST request
        pass
    elif request.method == "GET":
        # Handle GET request
         return render_template("enter_chat.html")



@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form.get('username')
    message = request.form.get('message')

    # Nachricht in die Datenbank einfügen
    cursor.execute("INSERT INTO messages (username, message) VALUES (?,?)", (username, message))
    conn.commit()

    return jsonify({'status': 'OK'})

@app.route('/get_messages')
def get_messages():
    cursor.execute("SELECT * FROM messages ORDER BY timestamp ASC")
    messages = cursor.fetchall()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run()