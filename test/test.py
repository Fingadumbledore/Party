from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    username = request.form["username"]
    
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()
    
    return render_template("index.html")

@app.route("/get")
def get():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT username, message, timestamp FROM messages")
    messages = c.fetchall()
    conn.close()
    
    return render_template("messages.html", messages=messages)

if __name__ == "__main__":
    app.run()
