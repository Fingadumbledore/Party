from flask import Flask, render_template, jsonify, request, session, redirect
from picker import picker as pick
import sqlite3
import os
import time
import qrcode
import shutil
import re
import numpy

starttime = 0
app = Flask(__name__, template_folder='templates/')
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
zeit = time.strftime("%H%M", time.localtime(time.time()))
app.config['SECRET_KEY'] = 'party'
matekiste = 0


def dbcon(sql):
    con = sqlite3.connect("party.db")
    warning_log("verbindung mit db wurde aufgenommen")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return sql.fetchall()

def ipfin():
    datei = open('ip.txt', 'r')
    print (datei.read())
    return datei.read()

def dbcon1(sql):
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    return cur.execute(sql)


def uptime():
    time = int(zeit)
    uptime = time - starttime
    return uptime


# log system
def log_server(log):
    log = date + " " + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()


def error_log(error):
    error = date + " [ERROR] " + error
    datei = open('server.log', 'a')
    datei.write('\n' + " " + error)
    log = date
    datei.close()


def problem_log(problem):
    problem = date + " [PROBLEM] " + problem
    datei = open('server.log', 'a')
    datei.write('\n' + " " + problem)
    log = date
    datei.close()


def warning_log(warning):
    warning = date + " [WARNING]" + warning
    datei = open('server.log', 'a')
    datei.write('\n' + " " + warning)
    log = date
    datei.close()


# Materechner Logic
def mate_logik(sorte, anzahl):
    if sorte == "Club Mate":
        koffeingehalt = 100

    if sorte == "Mio Mate":
        koffeingehalt = 100

    if sorte == "Flora Mate":
        koffeingehalt = 90

    if sorte == "Mate Mate":
        koffeingehalt = 150

    if sorte == "Buenos Mate":
        koffeingehalt = 100

    if sorte == "1337 Mate":
        koffeingehalt = 145

    if sorte == "Charitea Mate":
        koffeingehalt = 15

    if sorte == "Bionade Mate":
        koffeingehalt = 20

   
    '''
    anzahl = anzahl + 1
    koffeingehalt = 0
    match sorte:
        case "Mio Mio":
            koffeingehalt = '''


# mws = mate wirtschafts system
def mws(kisten):
    log_server("mws wurde angefragt")
    return mate


# Qr-code generator#
def create_qr(id):
    if not os.path.exists("./static/img/qr.png"):
        qip = ipfin()
        img = qrcode.make(f'{qip}:5000/session/{id}')
        type(img)
        img.save("./static/img/qr.png")
    else:
        warning_log("QR-Code ist bereits vorhanden")


# Hauptseite
@app.route("/")
def index():
    log_server("called /")
    return render_template("index.html")


# Neue Nachrichten
@app.route("/get_chat", methods=['POST'])
def get_chat():
    
        log_server("called /get_chat")
        log_server("called /get_chat with POST")
        userID = request.form['userid']
        sessionID = request.form['sessionid']
        message = request.form['message']
        zeit = date
        l = f"INSERT INTO seession (sessionname, sesionstatus, seessiontyp) VALUES(  \'{sessionID}\', \'{userID}\',\'{message}\', \'{zeit}\');"
        log_server("neue Nachricht")
        try:
            dbcon(l)
            log_server("message entered successfully")
        except Exception:
            error_log("unable to get new Messages")
        # account = cursor.fetchone()
        return render_template("chat.html")
  
@app.route("/get_game_file", methods=['POST'])
def get_game_file():
    log_server("called /get_game_file")
    pick()

@app.route("/get_new_message")
def get_new_message():

        log_server("called /get_new_message")
        return render_template("chat.html")
   
@app.route("/message")
def message():

        log_server("called /message")
        return render_template("message.html")
   
# planer
@app.route("/get_planer", methods=['POST'])
def get_planer():
    log_server("called /get_planer")
    log_server("called /get_planer with POST")
    event = request.form['event']
    sessionID = request.form['sessionID']
    zeit = request.form['zeit']
    pfad = "/session/" + sessionID
    status = "running"
    l = f"INSERT INTO planer VALUES(  \'{event}\', \'{zeit}\', \'{sessionID}\',\'{status}\');"
    log_server("neues Event")
    try:
        con = sqlite3.connect("party.db")
        warning_log("verbindung mit db wurde aufgenommen")
        cur = con.cursor()
        cur.execute(l)
        con.commit()
        con.close()
        log_server("event entered successfully /get_planer")
    except Exception:
        error_log("unable to insert event")
    return redirect(f'/session/{sessionID}')


@app.route("/session/<id>")
def _session(id):
    log_server(f"called /session/{id}")
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    l = f"SELECT eventname FROM planer WHERE sessionID = \'{id}\' ORDER BY eventzeit;"
    eventname = [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT eventzeit FROM planer WHERE sessionID = \'{id}\' ORDER BY eventzeit;"
    eventzeit = [i[0] for i in cur.execute(l).fetchall()]
    #eventtime = re.split(',', eventzeit)
    con.commit()

    creator =  [i[0] for i in cur.execute("SELECT username FROM user WHERE info = 'Host'").fetchall()]
    con.commit()

    l = f"SELECT count(username) FROM user WHERE sessionID = \'{id}\';"
    useranzahl = cur.execute(l).fetchall()

    l = f"SELECT matename, mateanzahl FROM mate WHERE sessionID = \'{id}\' ORDER BY mateanzahl;"
    mate =   cur.execute(l).fetchall()
    con.commit()

    l = f"SELECT  Spielname FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
    game = [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT userID FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
    user = [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT Spielaktivität FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
    aktivitaet = [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT username FROM user WHERE sessionID = \'{id}\';"
    unames =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT userID FROM user WHERE sessionID = \'{id}\';"
    uids =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT ZEIT FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
    zeit =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()


    l = f"SELECT Punkte FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
    p_punkte =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT Spielname FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
    p_game =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT Spielaktivität FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
    p_aktivitaet =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()

    l = f"SELECT userID FROM pointgame WHERE sessionID = \'{id}\'ORDER BY Punkte;"
    p_user =  [i[0] for i in cur.execute(l).fetchall()]
    con.commit()
    cur.close()


    class eventData:
        def __init__(self, evn, evz):
            self.eventname = evn
            self.eventzeit = evz

    class userData:
        def __init__(self, us, usid):
            self.unames = us
            self.uids = usid
    
    class gameData:
        def __init__(self, ga, akt, usr, ze):
            self.game = ga
            self.aktivitaet = akt
            self.user = usr
            self.zeit = ze

    class pointgameData:
        def __init__(self, ga, akt, usr, pu):
            self.p_game = ga
            self.p_aktivitaet = akt
            self.p_user = usr
            self.p_punkte = pu


    gameda = gameData(game, aktivitaet, user, zeit)
    pointgameda = pointgameData(p_game, p_aktivitaet, p_user, p_punkte)
    eventdata = eventData(eventname, eventzeit)
    userdat = eventData(unames, uids)

    return render_template("session.html",
                           zeit=zeit,
                           aktivitaet=aktivitaet,
                           user=user,
                           eventdata=eventdata,
                           gameda=gameda,
                           pointgameda=pointgameda,
                           userdat=userdat,
                           game=game,
                           useranzahl=useranzahl,
                           creator=creator,
                           mate=mate,
                           uids=uids,
                           unames=unames,
                           der=uptime())


@app.route("/mate", methods=['POST'])
def mate():
        log_server("called /mate")

   
        mateFlaschen = request.form['mateFlaschen']
        sessionId = request.form['sessionID']
        mateSorte = request.form['mateSorte']

        if mateSorte == "Club Mate" and mateFlaschen == 20:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "Mio Mio" and mateFlaschen == 12:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "Flora Mate" and mateFlaschen == 20:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "Mate Mate" and mateFlaschen == 20:
            martekiste + 1
            mws(martekiste)
        if mateSorte == "Buenos Mate" and mateFlaschen == 20:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "Charitea Mate" and mateFlaschen == 12:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "1337 Mate" and mateFlaschen == 20:
            matekiste + 1
            mws(matekiste)
        if mateSorte == "Bionade Mate" and mateFlaschen == 20:
            martekiste + 1
            mws(martekiste)

        mateSql = f"INSERT INTO mate VALUES (\"{mateSorte}\", \'{mateFlaschen}\', \'{sessionId}\');"
        try:
            con = sqlite3.connect("party.db")
            warning_log("Verbindung mit Datenbank wurde aufgenommen /mate")
            cur = con.cursor()
            cur.execute(mateSql)
            con.commit()
            con.close()

            mate_logik(mateSorte, mateFlaschen)
            log_server("mate wurde in Datenbank eingefügt")
        except sqlite3.Error as e:
            error_log(f"error while executing sql: {e}")
        return redirect(f'/session/{sessionId}')
    

@app.route("/drink", methods=['POST'])
def drink():
        log_server("called /drink")

        con = sqlite3.connect("party.db")
        warning_log("Verbindung mit Datenbank wurde aufgenommen /drink")
        cur = con.cursor()
        mateFlaschen = request.form['mateFlaschen']
        sessionId = request.form['sessionID']
        mateSorte = request.form['mateSorte']

        l3 = f"SELECT mateanzahl FROM mate WHERE sessionID = \'{sessionId}\' AND matename = \'{mateSorte}\';"
        manzahl = [i[0] for i in cur.execute(l3).fetchall()]
        f = [mateFlaschen]
        substracted = list()
        for intem1, item2 in zip(manzahl, f):
            substracted.append(intem1 - item2)

        k = substracted
     

        mateSql = f"UPDATE mate SET mateanzahl = \'{k}\' WHERE sessionID = \'{sessionId}\' AND matename = \'{mateSorte}\');"
        try:
            con = sqlite3.connect("party.db")
            warning_log("Verbindung mit Datenbank wurde aufgenommen /drink")
            cur = con.cursor()
            cur.execute(mateSql)
            con.commit()
            con.close()

            mate_logik(mateSorte, mateFlaschen)
            log_server("mate wurde in Datenbank eingefügt")
        except sqlite3.Error as e:
            error_log(f"error while executing sql: {e}")
        return redirect(f'/session/{sessionId}')
    


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


@app.route("/passwd")
def passwd():
    log_server("called /passwd")
    return render_template("passwd.html")


@app.route("/change")
def change():
    log_server("called /change")
    return render_template("changeSession.html")


@app.route("/create_session")
def create_session():
    log_server("called /create_session")
    return render_template("createSession.html")


@app.route("/get_creat_session", methods=['POST'])
def get_creat_session():
    log_server("called /get_creat_session with POST")
    Gsessionname = request.form['sessionname']
    GsessionID = request.form['sessionid']
    Gusername = "Host"
    Gusertype = "admin"  
    GuserId = 1
    Gstatus = "online"
    l1 = f'INSERT INTO seession VALUES({GsessionID}, \'{Gsessionname}\', \'online\', \'public\');'
    print(l1)
    log_server("neue Session")
    
    con = sqlite3.connect("party.db")
    warning_log("verbindung mit db wurde aufgenommen")
    cur = con.cursor()
    log_server("a")
    cur.execute(l1)
      
    log_server("f")
    user_count = +1
    starttime = int(zeit)
    create_qr(GsessionID)
    try:
            con = sqlite3.connect("party.db")
            warning_log("verbindung mit db wurde aufgenommen")
            cur = con.cursor()
            username = "Host"
            usertype = "admin"
            userId = 1
            l = f'INSERT INTO user (username, sessionID, info) VALUES (\'{username}\', {GsessionID}, \'{usertype}\');'
            cur.execute(l)
            con.commit()
            con.close()
    except e:
            warning_log("user admin konnte nicht angelegt werden")
    return redirect(f'/session/{GsessionID}')
    log_server("session successfully started")

    

@app.route("/login")
def login():
    log_server("called /login")
    return render_template("login.html")


@app.route("/stopuhr", methods=['POST'])
def stopuhr():
 
        log_server("called /stopuhr")
        spielName = request.form['spiel']
        art = request.form['art']
        zeit = request.form['zeit']
        userId = request.form['userid']
        sessionId = request.form['sessionID']
        l = f"INSERT INTO game VALUES(  \'{sessionId}\', \'{userId}\',\'{spielName}\',\'{art}\', \'{zeit}\');"
        try:
            warning_log("verbindung mit Datenbank wurde aufgenommen")
            dbcon(l)
            log_server("time entered successfully /stopuhr")
        except Exception:
            error_log("unable to run sql /stopuhr")
        return redirect(f'/session/{sessionId}')


@app.route("/pointGame", methods=['POST'])
def pointgame():
        userId = request.form['userid']
        sessionId = request.form['sessionID']
        l = f"INSERT INTO pointgame VALUES(  \'{sessionId}\', \'{userId}\',\'{spielName}\',\'{art}\', \'{punkte}\');"
        try:
            warning_log("verbindung mit Datenbank wurde aufgenommen")
            dbcon(l)
            log_server("time entered successfully /pointGame")
        except Exception:
            error_log("unable to run sql /pointGame")
        return redirect(f'/session/{sessionId}')
  


@app.route("/get_event", methods=['POST'])
def get_event():

        log_server("called /get_event")
        event = request.form['event']
        zeit = request.form['zeit']
        sessionId = request.form['sessionid']
        l = f"INSERT INTO game VALUES(  \'{event}\', \'{zeit}\', \'{sessionId}\');"
        try:
            con = sqlite3.connect("party.db")
            warning_log("verbindung mit db wurde aufgenommen")
            cur = con.cursor()
            cur.execute(l)
            con.commit()
            con.close()
            log_server("event entered successfully /get_event")
        except e:
            error_log("unable to run sql /get_event")
        return render_template("login.html")
    


@app.route("/controll")
def controll():
    
        log_server("called /controll")
        return render_template("controll.html")
  

@app.route("/game")
def game():
    
        log_server("called /game")
        return render_template("game.html")



@app.route("/rgb")
def rgb():
    
        log_server("called /rgb")
        return render_template("404.html")


@app.route("/get_login", methods=['POST'])
def get_login():
    log_server("called /get_login with POST")
    username = request.form['username']
    sessionId = request.form['sessionID']
    userid = request.form['userID']
    l = f"select * from user where userID = \'{userid}\' and username=\'{username}\' and sessionID=\'{sessionId}\';"
    con = sqlite3.connect("party.db")
    warning_log("verbindung mit db wurde aufgenommen")
    cur = con.cursor()
    cur.execute(l)
    con.commit()
    con.close()
    # session['username'] = account['username']
    log_server("loggedin successfully")
    return redirect(f'/session/{sessionId}')

    con.close()


@app.route("/new", methods=['POST'])
def new():
    log_server("called /new with POST")
    username = request.form['username']
    sessionId = request.form['sessionID']
    userId = request.form['sessionID']
    info = "normal"
    l = f"INSERT INTO user(username, sessionID, info) VALUES (\'{username}\',\'{sessionId}\',\'{info}\');"
    con = sqlite3.connect("party.db")
    warning_log("verbindung mit db wurde aufgenommen")
    cur = con.cursor()
    cur.execute(l)
    con.commit()
    con.close()
    account = True

    # session['username'] = account['username']
    log_server("created new user successfully")
    return redirect(f'/session/{sessionId}')

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


# Use this line to run it localy

runip = ipfin()
app.run(host=runip, port=80)