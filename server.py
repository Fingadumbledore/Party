import sqlite3
import os
import time
#import qrcode
from flask import Flask, render_template, request, redirect
from picker import picker as pick
from database import dbcon, return_dbcon
from mate import mate_logik, mws
from log import log_server
#from picker import createChart

# Funktion um den Server zu machen
def server():
    starttime = 0
    app = Flask(__name__, template_folder='templates/')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    zeit = time.strftime("%H%M", time.localtime(time.time()))
    app.config['SECRET_KEY'] = 'party'
    matekiste = 0

    # hohlt die Ip-adresse aus einer Datei
    def ipfin():
        datei = open('ip.txt', 'r')
        print (datei.read())
        return datei.read()

    # Soll die uptime berechnen, wird in javascript neu gemacht
    def uptime(): 
        return int(zeit) - starttime

    # Qr-code generator#
    #def create_qr(id):
       # if not os.path.exists("./static/img/qr.png"):
        #    qip = ipfin()
        #    img = qrcode.make(f'{qip}:80/session/{id}')
       #     type(img)
       #     img.save("./static/img/qr.png")
     #   else:
        #    log_server("QR-Code ist bereits vorhanden", "WARNING")

    # Hauptseite
    @app.route("/")
    def index():
        log_server("called /", "INFO")
        return render_template("index.html")

    # Neue Nachrichten
    @app.route("/get_chat", methods=['POST'])
    def get_chat():
            log_server("called /get_chat", "INFO")
            log_server("called /get_chat with POST", "INFO")
            userID = request.form['userid']
            sessionID = request.form['sessionid']
            message = request.form['message']
            zeit = date
            l = f"INSERT INTO seession (sessionname, sesionstatus, seessiontyp) VALUES(  \'{sessionID}\', \'{userID}\',\'{message}\', \'{zeit}\');"
            log_server("neue Nachricht", "INFO")
            try:
                dbcon(l)
                log_server("message entered successfully", "INFO")
            except Exception:
                log_server("unable to get new Messages", "ERROR")
            # account = cursor.fetchone()
            return render_template("chat.html")
    
    # Um in der Zukunft spiele dateien zu bekommen
    @app.route("/get_game_file", methods=['POST'])
    def get_game_file():
        log_server("called /get_game_file", "INFO")
        pick()
    # Neue Nachrichten zu bekommen
    @app.route("/get_new_message")
    def get_new_message():
            log_server("called /get_new_message", "INFO")
            return render_template("chat.html")
   
    # Macht message.html sichtbar
    @app.route("/message")
    def message():
            log_server("called /message", "INFO")
            return render_template("message.html")

    # hier planer sachen in die Datenbank geschoben
    @app.route("/get_planer", methods=['POST'])
    def get_planer():
        log_server("called /get_planer", "INFO")
        log_server("called /get_planer with POST", "INFO")
        event = request.form['event']
        sessionID = request.form['sessionID']
        zeit = request.form['zeit']
        pfad = "/session/" + sessionID
        status = "running"
        l = f"INSERT INTO planer VALUES(  \'{event}\', \'{zeit}\', \'{sessionID}\',\'{status}\');"
        log_server("neues Event", "INFO")
        try:
            dbcon(l)
            log_server("event entered successfully /get_planer", "INFO")
        except Exception:
            log_server("unable to insert event", "ERROR")
        return redirect(f'/session/{sessionID}')

    # Das Zeit die Session seite an. Außerdem werden hier daten mit Jinja ans Frontend geschickt
    @app.route("/session/<id>")
    def _session(id):
        def values(l: str):
            return [i[0] for i in return_dbcon(l)]
        #print(os.cpu_count())
        #createChart("41", "NFSU2")
        log_server(f"called /session/{id}", "INFO")
        con = sqlite3.connect("party.db")
        cur = con.cursor()
        l = f"SELECT eventname FROM planer WHERE sessionID = \'{id}\' ORDER BY eventzeit;"
        eventname = values(l)

        l = f"SELECT eventzeit FROM planer WHERE sessionID = \'{id}\' ORDER BY eventzeit;"
        eventzeit = values(l)

        l =  "SELECT username FROM user WHERE info = 'Host'"
        creator = values(l)
        con.commit()

        l = f"SELECT count(username) FROM user WHERE sessionID = \'{id}\';"
        useranzahl = return_dbcon(l)

        l = f"SELECT matename, mateanzahl FROM mate WHERE sessionID = \'{id}\' ORDER BY mateanzahl;"
        mate = return_dbcon(l)

        l = f"SELECT  Spielname FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
        game = values(l)

        l = f"SELECT userID FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
        user = values(l)

        l = f"SELECT Spielaktivität FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
        aktivitaet = values(l)

        l = f"SELECT username FROM user WHERE sessionID = \'{id}\';"
        unames = values(l) 

        l = f"SELECT userID FROM user WHERE sessionID = \'{id}\';"
        uids = values(l)

        l = f"SELECT ZEIT FROM game WHERE sessionID = \'{id}\' ORDER BY ZEIT;"
        zeit = values(l)

        l = f"SELECT Punkte FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
        p_punkte = values(l)

        l = f"SELECT Spielname FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
        p_game = values(l)

        l = f"SELECT Spielaktivität FROM pointgame WHERE sessionID = \'{id}\' ORDER BY Punkte;"
        p_aktivitaet = values(l)

        l = f"SELECT userID FROM pointgame WHERE sessionID = \'{id}\'ORDER BY Punkte;"
        p_user = values(l)
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

    # Dies fügt mate hinzu, und macht bei der richtigen Anzahl einen kasten daraus
    @app.route("/mate", methods=['POST'])
    def mate():
            log_server("called /mate", "INFO")
            mateFlaschen = request.form['mateFlaschen']
            sessionId = request.form['sessionID']
            mateSorte = request.form['mateSorte']
            mateSql = f"INSERT INTO mate VALUES (\"{mateSorte}\", \'{mateFlaschen}\', \'{sessionId}\');"
            try:
                dbcon(mateSql)

                mate_logik(mateSorte, mateFlaschen)
                log_server("mate wurde in Datenbank eingefügt", "INFO")
            except sqlite3.Error as e:
                log_server(f"error while executing sql: {e}", "WARNING")
            return redirect(f'/session/{sessionId}')
        
    # Hier ist ein Teil der Matelogic, wenn eine Person eine Mate trinkt wird das in der Datenbank vermerkt, und es ist eine Flasche weniger da. Dies geht zum teil noch in die mate.py
    @app.route("/drink", methods=['POST'])
    def drink():
            log_server("called /drink", "INFO")
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
                dbcon(mateSql)
                mate_logik(mateSorte, mateFlaschen)
                log_server("mate wurde in Datenbank eingefügt", "ERROR")
            except sqlite3.Error as e:
                log_server(f"error while executing sql: {e}", "ERROR")
            return redirect(f'/session/{sessionId}')
        
    # Dies zeigt die Logout Seite
    @app.route("/logout")
    def logout():
        log_server("called /logout", "INFO")
        user_count = -1
        return render_template("logout.html")

    # Das hier zeigt die Seite an auf der Spiele hinzugefügt werden können
    @app.route("/spiel")
    def spiel():
        log_server("called /spiel", "INFO")
        user_count = -1
        spiel = "Tomb raider"
        return render_template("spiel.html", spiel=spiel,)

    # Hier werden die Spiele hinzugefügt
    @app.route("/get_spiel")
    def get_spiel():
        log_server("called /get_spiel", "INFO")
        return render_template("spiel.html")

    # Diese seite mahnt den User sich anzumelden um den Inhalt zu sehen
    @app.route("/passwd")
    def passwd():
        log_server("called /passwd", "INFO")
        return render_template("passwd.html")

    # Hier ist eine Seite die zum wechseln einer Session dient
    @app.route("/change")
    def change():
        log_server("called /change", "INFO")
        return render_template("changeSession.html")

    # Hier wird die Seite zum erstellen einer Session erstellt
    @app.route("/create_session")
    def create_session():
        log_server("called /create_session", "INFO")
        return render_template("createSession.html")

    # Hier wird die Session erstellt
    @app.route("/get_creat_session", methods=['POST'])
    def get_creat_session():
        log_server("called /get_creat_session with POST", "INFO")
        Gsessionname = request.form['sessionname']
        GsessionID = request.form['sessionid']
        Gusername = "Host"
        Gusertype = "admin"  
        GuserId = 1
        Gstatus = "online"
        l1 = f'INSERT INTO seession VALUES({GsessionID}, \'{Gsessionname}\', \'online\', \'public\');'
        print(l1)
        log_server("neue Session", "INFO")
        
        dbcon(l1)
        
        user_count = +1
        starttime = int(zeit)
        try:
                username = "Host"
                usertype = "admin"
                userId = 1
                l = f'INSERT INTO user (username, sessionID, info) VALUES (\'{username}\', {GsessionID}, \'{usertype}\');'
                dbcon(l)
        except e:
                log_server("User Admin konnte nicht angelegt werden", "WARNING")
        return redirect(f'/session/{GsessionID}')
        log_server("session successfully started", "INFO")

    # Hier soll später für Spiele Charts geschickt werden. Dafür gibt es in statistik.py sachen
    @app.route("/charts")
    def charts():
        log_server("called /charts", "INFO")
        csessionID = request.form['sessionID']
        k = f"SELCT COUNT(DISTINCT 'Spielname') FROM game WHERE sessionID = \'{csessionID}\';"
        dbcon(k)
        return redirect(f'/session/{csessionID}')  

    # Hierdurch wird die Login/Join seite angezeit
    @app.route("/login")
    def login():
        log_server("called /login", "INFO")
        return render_template("login.html")

    # Hier werden Spiele die nach Zeit gehen, in die Datenbank eingetragen
    @app.route("/stopuhr", methods=['POST'])
    def stopuhr():
            log_server("called /stopuhr", "INFO")
            spielName = request.form['spiel']
            art = request.form['art']
            zeit = request.form['zeit']
            userId = request.form['userid']
            sessionId = request.form['sessionID']
            l = f"INSERT INTO game VALUES(  \'{sessionId}\', \'{userId}\',\'{spielName}\',\'{art}\', \'{zeit}\');"
            try:
                log_server("Verbindung mit Datenbank wurde aufgenommen", "WARNING")
                dbcon(l)
                log_server("time entered successfully /stopuhr", "INFO")
            except Exception:
                log_server("unable to run sql /stopuhr", "ERROR")
            return redirect(f'/session/{sessionId}')

    # Hier werden die Daten für Spiele die Nach Punkten gehe, in die Datenbank eingetragen
    @app.route("/pointGame", methods=['POST'])
    def pointgame():
            userId = request.form['userid']
            sessionId = request.form['sessionID']
            l = f"INSERT INTO pointgame VALUES(  \'{sessionId}\', \'{userId}\',\'{spielName}\',\'{art}\', \'{punkte}\');"
            try:
                log_server("Verbindung mit Datenbank wurde aufgenommen", "WARNING")
                dbcon(l)
                log_server("time entered successfully /pointGame", "INFO")
            except Exception:
                log_server("unable to run sql /pointGame", "ERROR")
            return redirect(f'/session/{sessionId}')
    

    # Hier werden Events vom Planer hinzugefügt
    @app.route("/get_event", methods=['POST'])
    def get_event():

            log_server("called /get_event", "INFO")
            event = request.form['event']
            zeit = request.form['zeit']
            sessionId = request.form['sessionid']
            l = f"INSERT INTO game VALUES(  \'{event}\', \'{zeit}\', \'{sessionId}\');"
            try:
                dbcon(l)
                log_server("event entered successfully /get_event", "INFO")
            except e:
                log_server("unable to run sql /get_event", "ERROR")
            return render_template("login.html")
        
    # Hier soll später der RGB Streifen angesteuert werden am Raspberry pi
    @app.route("/rgb")
    def rgb():
            log_server("called /rgb", "INFO")
            return render_template("404.html")

    # Hier ist der Login in eine Session
    @app.route("/get_login", methods=['POST'])
    def get_login():
        log_server("called /get_login with POST", "INFO")
        username = request.form['username']
        sessionId = request.form['sessionID']
        userid = request.form['userID']
        l = f"select * from user where userID = \'{userid}\' and username=\'{username}\' and sessionID=\'{sessionId}\';"
        dbcon(l)
        # session['username'] = account['username']
        log_server("loggedin successfully", "INFO")
        return redirect(f'/session/{sessionId}')

        con.close()

    # Hier wird ein neuer User angelegt
    @app.route("/new", methods=['POST'])
    def new():
        log_server("called /new with POST", "INFO")
        username = request.form['username']
        sessionId = request.form['sessionID']
        userId = request.form['sessionID']
        l = f"INSERT INTO user(username, sessionID, info) VALUES (\'{username}\',\'{sessionId}\',info);"
        dbcon(l)
        account = True

        # session['username'] = account['username']
        log_server("created new user successfully", "INFO")
        return redirect(f'/session/{sessionId}')

        con.close()

    #  Hier soll es möglich sein, Dateien hochzuladen wie bei einem Nas
    @app.route("/upload_file", methods=["POST"])
    def upload_file():
        log_server("called /upload_file with POST", "INFO")
        """
        log_server("called /upload_file")
        file = request.files
        print(f"{file=}")
        return render_template(f'404.html')"""
        file = request.files["file"]
        print (file)
        
        if file and file.filename:
            file.save("/Export", file.filename)
            return "File uploaded successfully!"
        return "No file found"

    #Hier kommen die Chat Nachrichten an
    @app.route("/send", methods=["POST"])
    def send():
        log_server("called /send with POST", "INFO")
        message = request.form["message"]
        username = request.form["username"]
        
        conn = sqlite3.connect("party.party.db")
        c = conn.cursor()
        c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
        conn.commit()
        conn.close()
        
        return render_template("index.html")

    # Hier werden die Chat Nachrichten Verschickt
    @app.route("/get")
    def get():
        log_server("called /get with GET", "INFO")
        conn = sqlite3.connect("party.db")
        c = conn.cursor()
        c.execute("SELECT username, message, timestamp FROM messages")
        messages = c.fetchall()
        conn.close()
        return render_template("messages.html", messages=messages)


    # Soll Musik Daten schicken
    @app.route("/music/<int:id>")
    def get_music(id):
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM music WHERE id=?", (id,))
        music = cursor.fetchone()
        conn.close()
        return send_file(music[1], attachment_filename=music[2], as_attachment=True)

    # Gibt die 404 Seite aus, wenn es Seite nicht gibt
    @app.errorhandler(404)
    def page_not_found(e):
        log_server("called non-existing page", "ERROR")
        return render_template('404.html'), 404


    # Use this line to run it localy
    runip = ipfin()
    app.run(host=runip, port=8080)

if __name__ == "__main__":
	print("Use main.py to use program")
