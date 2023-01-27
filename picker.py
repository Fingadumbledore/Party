import shutil, os
import matplotlib.pyplot as plt
import sqlite3


def dbcon(sqlstring):
    print ("test")
    try:
        con = sqlite3.connect("party.db")
        cur = con.cursor()
        cur.execute(sqlstring)
    except:
        return "error"

def tmbr():
    print("tomb raider datei")
    f = "sql"
    dbcon(f)

def nfsu2():
    print("nfsu2 datei")
    e = "sql"
    dbcon(e)

def anno1602():
    print("Anno 1602 datei")
    a = "sql"
    dbcon(a)

def picker(gamefile, sessionID, SpielerID):
    datei = open(gamefile, 'a')

    if  check == "nfsu2":
        nfsu2()
    if check == "anno16":
        anno1602()
    if check == tmbr:
        tmbr()
    
    if not os.path.exists(sessionID):
        os.makedirs(sessionID)
    shutil.move(gamefile, sessionID)


def createChart(sessionID,Spielname):   
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    dateiname = sessionID + Spielname + ".png"
    try:
        l = f"SELECT 'username' FROM user INNER JOIN game ON game.userID = user.userID;"
        user = [i[0] for i in cur.execute(l).fetchall()]
    except:
        print("Fehler beim Ausführen von:" + l)  
    try:
        l = f"SELECT ZEIT FROM game WHERE sessionID = \'{sessionID}\' AND Spielname = \'{Spielname}\';"
        zeit = [i[0] for i in cur.execute(l).fetchall()]
    except:
        print("Fehler beim Ausführen von:" + l)  

    colors = ['green','blue','purple','brown','teal', 'yellow', 'black', 'orange']
    plt.bar(user, zeit, color=colors)
    plt.title(Spielname, fontsize=14)
    plt.xlabel('User', fontsize=14)
    plt.ylabel('Zeit in Sekunden', fontsize=14)
    plt.grid(False)
    plt.savefig(dateiname)
    

if __name__ == "__main__":
	print("Use main.py to use program")