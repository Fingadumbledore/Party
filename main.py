from flask import Flask, render_template, jsonify, request, session, redirect
import sqlite3
import time

app = Flask(__name__, template_folder='templates/')
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date
app.config['SECRET_KEY'] = 'party'


def log_server(log):
    log = date + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

@app.route("/")
def index():
    log_server("called /")
    return render_template("index.html")

#Chat
@app.route("/chat")
def chat():
    log_server("called /chat")
    return render_template("chat.html")

@app.route("/get_chat", methods=['POST'])
def get_chat():
    log_server("called /get_chat")
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    log_server("called /get_creat_session with POST")

    userID = request.form['userid']
    sessionID = request.form['sessionid']
    message = request.form['message']
    zeit = date
    l = f"INSERT INTO session VALUES(  \'{sessionID}\', \'{userID}\',\'{message}\', \'{zeit}\');"
    log_server("neue Nachricht")

    cur.execute(l)
    account = cur.fetchone()
    return render_template("chat.html")

@app.route("/get_new_message")
def get_new_message():
    log_server("called /get_new_message")
    return render_template("chat.html")    

#planer
@app.route("/planer")
def planer():
    log_server("called /planer")
    return render_template("planer.html")

@app.route("/get_planer", methods=['POST'])
def get_planer():
    log_server("called /get_planer")
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    log_server("called /get_planer with POST")

    event = request.form['event']
    sessionID = request.form['sessionid']
    zeit = request.form['zeit']
    l = f"INSERT INTO session VALUES(  \'{event}\', \'{zeit}\',\'{sessionID}\');"
    log_server("neues Event")
    cur.execute(l)
    account = cur.fetchone()
    return render_template("chat.html")

@app.route("/session")
def session():
    log_server("called /session")
    return render_template("session.html")

@app.route("/logout")
def logout():
    log_server("called /logout")
    return render_template("logout.html")

@app.route("/signin")
def signin():
    log_server("called /signin")
    return render_template("signin.html")

@app.route("/password")
def password():
    log_server("called /password")
    return render_template("passwort_ver.html")

@app.route("/create_session")
def create_session():
    log_server("called /create_session")
    return render_template("createSession.html")

@app.route("/get_creat_session", methods=['POST'])
def get_creat_session():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    log_server("called /get_creat_session with POST")

    sessionname = request.form['sessionname']
    sessionID = request.form['sessionid']
    l = f"INSERT INTO session VALUES(  \'{sessionID}\', \'{sessionname}\');"
    log_server("neue Session")
    cur.execute(l)
    account = cur.fetchone()
    return redirect('/session')
    

@app.route("/login")
def login():
    log_server("called /login")
    return render_template("login.html")

@app.route("/stopuhr", methods=['POST'])
def stopuhr():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    log_server("called /stopuhr")
    spielName = request.form['spielname']
    zeit = request.form['zeit']
    userId = request.form['userid']
    sessionId = request.form['sessionid']
    l = f"INSERT INTO game VALUES(  \'{sessionID}\', \'{userId}\',\'{spielName}\', \'{zeit}\');"
    return render_template("login.html")

@app.route("/get_event", methods=['POST'])
def get_event():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    log_server("called /get_event")
    event = request.form['event']
    zeit = request.form['zeit']
    sessionId = request.form['sessionid']
    l = f"INSERT INTO game VALUES(  \'{event}\', \'{zeit}\', \'{sessionId}\');"
    return render_template("login.html")

@app.route("/controll")
def controll():
    log_server("called /login")
    return render_template("controll.html")

@app.route("/rgb")
def rgb():
    log_server("called /rgb")
    return render_template("404.html")


@app.route("/get_login", methods=['POST'])
def get_login():
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    log_server("called /get_login with POST")

    username = request.form['uname']
    sessionId = request.form['id']
    l = f"select * from user where username = \'{username}\' and id=\'{sessionId}\';"

    cur.execute(l)
    account = cur.fetchone()

    if account:
        session['loggedin'] = True
        # session['username'] = account['username']
        return redirect('/session')
    else:
        return "{ \"message\": \"Login failed\"'}"
    con.close()

@app.errorhandler(404)
def page_not_found(e):
    log_server("called non-existing page")
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def create_app(config_filename):
    app.register_error_handler(404, page_not_found)
    log_server("created app")
    return app
