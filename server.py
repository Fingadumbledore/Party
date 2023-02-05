from flask import Flask, render_template, jsonify, request, session, redirect
from picker import picker as pick
from picker import createChart
import sqlite3
import os
import time
import qrcode
import shutil
import re
import numpy

def server():
    starttime = 0
    app = Flask(__name__, template_folder='templates/')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    zeit = time.strftime("%H%M", time.localtime(time.time()))
    app.config['SECRET_KEY'] = 'party'
    matekiste = 0


    def dbcon(sql):
        try:
            con = sqlite3.connect("party.db")
            log_server("dbcon hat die Verbindung mit db aufgenommen", "WARNING")
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except:
            return "ERROR"

    def ipfin():
        datei = open('ip.txt', 'r')
        print (datei.read())
        return datei.read()

    def return_dbcon(sql):
        try:
            con = sqlite3.connect("party.db")
            log_server("return_dbcon hat die Verbindung mit db aufgenommen", "WARNING")
            cur = con.cursor()
            ergebnis = cur.execute(sql).fetchall()
            con.commit()
            return ergebnis
        except:
            return "Error"

    def uptime(): 
        return int(zeit) - starttime

    # log system
    def log_server(log, type):
        log = date + ' [' + type + '] ' + log
        datei = open('server.log', 'a')
        datei.write('\n' + " " + log)
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
        log_server("mws wurde angefragt", "INFO")
        return mate


    def sessionBeenden(sessionID):
        con = sqlite3.connect("party.db")
        log_server("verbindung mit db wurde aufgenommen", "WARNING")
        cur = con.cursor()
        os.makedirs(sessionID)
        

    # Qr-code generator#
    def create_qr(id):
        if not os.path.exists("./static/img/qr.png"):
            qip = ipfin()
            img = qrcode.make(f'{qip}:80/session/{id}')
            type(img)
            img.save("./static/img/qr.png")
        else:
            log_server("QR-Code ist bereits vorhanden", "WARNING")


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
    
    @app.route("/get_game_file", methods=['POST'])
    def get_game_file():
        log_server("called /get_game_file", "INFO")
        pick()

    @app.route("/get_new_message")
    def get_new_message():

            log_server("called /get_new_message", "INFO")
            return render_template("chat.html")
    
    @app.route("/message")
    def message():

            log_server("called /message", "INFO")
            return render_template("message.html")

    # planer
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


    @app.route("/mate", methods=['POST'])
    def mate():
            log_server("called /mate", "INFO")

    
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
                dbcon(mateSql)

                mate_logik(mateSorte, mateFlaschen)
                log_server("mate wurde in Datenbank eingefügt", "INFO")
            except sqlite3.Error as e:
                log_server(f"error while executing sql: {e}", "WARNING")
            return redirect(f'/session/{sessionId}')
        

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
        


    @app.route("/logout")
    def logout():
        log_server("called /logout", "INFO")
        user_count = -1
        return render_template("logout.html")

    @app.route("/spiel")
    def spiel():
        log_server("called /spiel", "INFO")
        user_count = -1
        spiel = "Tomb raider"
        return render_template("spiel.html", spiel=spiel,)

    @app.route("/get_spiel")
    def get_spiel():
        log_server("called /get_spiel", "INFO")
        return render_template("spielt.html")



    @app.route("/signin")
    def signin():
        log_server("called /signin", "INFO")
        return render_template("signin.html")


    @app.route("/password")
    def password():
        log_server("called /password", "INFO")
        return render_template("passwort_ver.html")


    @app.route("/passwd")
    def passwd():
        log_server("called /passwd", "INFO")
        return render_template("passwd.html")


    @app.route("/change")
    def change():
        log_server("called /change", "INFO")
        return render_template("changeSession.html")


    @app.route("/create_session")
    def create_session():
        log_server("called /create_session", "INFO")
        return render_template("createSession.html")


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
        create_qr(GsessionID)
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

    @app.route("/charts")
    def charts():
        log_server("called /charts", "INFO")
        csessionID = request.form['sessionID']
        k = f"SELCT COUNT(DISTINCT 'Spielname') FROM game WHERE sessionID = \'{csessionID}\';"
        dbcon(k)
        return redirect(f'/session/{csessionID}')  

    @app.route("/login")
    def login():
        log_server("called /login", "INFO")
        return render_template("login.html")


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
        


    @app.route("/controll")
    def controll():
        
            log_server("called /controll", "INFO")
            return render_template("controll.html")

    @app.route("/statistik", methods=['POST'])
    def statistik():
            sessionId = request.form['id']
            game = request.form['game']
            createChart(sessionId, game)
            log_server("called /statistik", "INFO")
            return render_template("controll.html")
    

    @app.route("/game")
    def game():
        
            log_server("called /game", "INFO")
            return render_template("game.html")



    @app.route("/rgb")
    def rgb():
            log_server("called /rgb", "INFO")
            return render_template("404.html")


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


    @app.route("/new", methods=['POST'])
    def new():
        log_server("called /new with POST", "INFO")
        username = request.form['username']
        sessionId = 
        userId = request.form['sessionID']
        l = f"INSERT INTO user(username, sessionID, info) VALUES (\'{username}\',\'{sessionId}\',info);"
        dbcon(l)
        account = True

        # session['username'] = account['username']
        log_server("created new user successfully", "INFO")
        return redirect(f'/session/{sessionId}')

        con.close()

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
        
        if file:
            file.save("/Export", file.filename)
            return "File uploaded successfully!"
        return "No file found"

    @app.route("/send", methods=["POST"])
    def send():
        log_server("called /send with POST", "INFO")
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
        log_server("called /get with GET", "INFO")
        conn = sqlite3.connect("chat.db")
        c = conn.cursor()
        c.execute("SELECT username, message, timestamp FROM messages")
        messages = c.fetchall()
        conn.close()
        
        return render_template("messages.html", messages=messages)

    @app.route("/chat")
    def chat():
        log_server("called /chat","INFO")
        return render_template("chat.html")

    @app.route("/music/<int:id>")
    def get_music(id):
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM music WHERE id=?", (id,))
        music = cursor.fetchone()
        conn.close()
        return send_file(music[1], attachment_filename=music[2], as_attachment=True)


    @app.errorhandler(404)
    def page_not_found(e):
        log_server("called non-existing page", "ERROR")
        return render_template('404.html'), 404


    def create_app(config_filename):
        app.register_error_handler(404, page_not_found)
        log_server("created app", "INFO")
        return app


    # Use this line to run it localy

    runip = ipfin()
    app.run(host=runip, port=80)

if __name__ == "__main__":
	print("Use main.py to use program")
