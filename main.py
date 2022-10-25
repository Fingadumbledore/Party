from flask import Flask, render_template, jsonify, request, session, redirect
import sqlite3
import os
import time
import qrcode
import shutil

starttime = 0
user_count = 0
app = Flask(__name__, template_folder='templates/')
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
zeit = time.strftime("%H%M", time.localtime(time.time()))
log = date
app.config['SECRET_KEY'] = 'party'

def dbcon(sql):
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    cur.execute(sql)
    return sql.fetchall()

def uptime():
    time = int(zeit)
    uptime = time - starttime
    return uptime

#log system
def log_server(log):
    log = date + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

def error_log(error):
    error = date + " [ERROR]"+ error
    datei = open('server.log', 'a')
    datei.write('\n' + " " + error)
    log = date
    datei.close()  

def problem_log(problem):
    problem = date + " [PROBLEM]"+ problem
    datei = open('server.log', 'a')
    datei.write('\n' + " " + problem)
    log = date
    datei.close() 

def warning_log(warning):
    warning = date + " [WARNING]"+ warning
    datei = open('server.log', 'a')
    datei.write('\n' + " " + warning)
    log = date
    datei.close()  

# Qr-code generator
if not os.path.exists("./static/img/qr.png"):
    img = qrcode.make('127.0.0.1:5000')
    type(img)
    img.save("qr.png")
    ort = "./static/img"
    shutil.move("qr.png", ort)
else:
    warning_log("QR-Code ist bereits vorhanden")

#Hauptseite
@app.route("/")
def index():
    log_server("called /")
    return render_template("index.html")

#Chat
@app.route("/chat")
def chat():
    log_server("called /chat")
    return render_template("chat.html")
#Neue Nachrichten
@app.route("/get_chat", methods=['POST'])
def get_chat():
    log_server("called /get_chat")
    log_server("called /get_chat with POST")
    userID = request.form['userid']
    sessionID = request.form['sessionid']
    message = request.form['message']
    zeit = date
    l = f"INSERT INTO session VALUES(  \'{sessionID}\', \'{userID}\',\'{message}\', \'{zeit}\');"
    log_server("neue Nachricht")
    try:
        dbcon(l)
    except:
        error_log("unable to get new Messages")
    account = cur.fetchone()
    return render_template("chat.html")

@app.route("/get_new_message")
def get_new_message():
    log_server("called /get_new_message")
    return render_template("chat.html")    

@app.route("/message")
def message():
    log_server("called /message")
    return render_template("message.html")

#planer
@app.route("/planer")
def planer():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    asd = cur.execute('SELECT * FROM planer').fetchall()
    cur.close()
    log_server("called /planer")
    return render_template("planer.html", asd=asd)

@app.route("/get_planer", methods=['POST'])
def get_planer():
    log_server("called /get_planer")
    log_server("called /get_planer with POST")
    event = request.form['event']
    sessionID = request.form['sessionid']
    zeit = request.form['zeit']
    l = f"INSERT INTO session VALUES(  \'{event}\', \'{zeit}\',\'{sessionID}\');"
    log_server("neues Event")
    try:
        dbcon(l)
    except:
        error_log("unable to insert event")
    account = cur.fetchone()
    return render_template("chat.html")

@app.route("/session")
def session():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    die = cur.execute("SELECT sessionname FROM session").fetchall()
    log_server("called /session")
    return render_template("session.html", die=die)

@app.route("/logout")
def logout():
    log_server("called /logout")
    user_count = -1
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
    log_server("called /get_creat_session with POST")
    sessionname = request.form['sessionname']
    sessionID = request.form['sessionid']
    l = f"INSERT INTO session VALUES(  \'{sessionID}\', \'{sessionname}\');"
    log_server("neue Session")
    try:
          account = dbcon(l)   
    except:
        error_log("unable to create Session")
    user_count = +1
    starttime = int(zeit)
    return redirect('/session')
    
@app.route("/login")
def login():
    log_server("called /login")
    return render_template("login.html")

@app.route("/stopuhr", methods=['POST'])
def stopuhr():
    log_server("called /stopuhr")
    spielName = request.form['spielname']
    zeit = request.form['zeit']
    userId = request.form['userid']
    sessionId = request.form['sessionid']
    l = f"INSERT INTO game VALUES(  \'{sessionID}\', \'{userId}\',\'{spielName}\', \'{zeit}\');"
    try:
        dbcon(l)
    except:
        error_log("unable to run sql /stopuhr")
    return render_template()

@app.route("/get_event", methods=['POST'])
def get_event():
    log_server("called /get_event")
    event = request.form['event']
    zeit = request.form['zeit']
    sessionId = request.form['sessionid']
    l = f"INSERT INTO game VALUES(  \'{event}\', \'{zeit}\', \'{sessionId}\');"
    try:
        dbcon(l)
    except:
        error_log("unable to run sql /get_event")
    return render_template("login.html")

@app.route("/controll")
def controll():
    log_server("called /login")
    return render_template("controll.html")

@app.route("/game")
def game():
    log_server("called /game")
    return render_template("game.html")

@app.route("/willkommen")
def willkommen():
    log_server("called /willkommen")
    return render_template("willkommen.html")

@app.route("/seession")
def seession():
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    creator = cur.execute("SELECT username FROM user WHERE info = 'creator'").fetchall()
    cur.close()
    log_server("called /session")
    return render_template("seesion.html", das=user_count, er=creator, der=uptime())

@app.route("/rgb")
def rgb():
    log_server("called /rgb")
    return render_template("404.html")

@app.route("/get_login", methods=['POST'])
def get_login():
    log_server("called /get_login with POST")
    username = request.form['uname']
    sessionId = request.form['id']
    l = f"select * from user where username = \'{username}\' and id=\'{sessionId}\';"
    account = dbcon(l)
    if account:
        session['loggedin'] = True
        user_count = +1
        # session['username'] = account['username']
        return redirect('/session')
    else:
        return "{ \"message\": \"Login failed\"'}"
    con.close()

@app.errorhandler(404)
def page_not_found(e):
    error_log("called non-existing page")
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

def create_app(config_filename):
    app.register_error_handler(404, page_not_found)
    log_server("created app")
    return app