import matplotlib.pyplot as plt

def create_chart(session_id,spiel_name):
    """ create chart of game """
    con = sqlite3.connect("party.db")
    cur = con.cursor()
    dateiname = session_id + spiel_name + ".png"
    try:
        l = f"SELECT 'username' FROM user INNER JOIN game ON game.userID = user.userID;"
        user = [i[0] for i in cur.execute(l).fetchall()]
    except:
        print("Fehler beim Ausführen von:" + l)
    try:
        l = f"""SELECT ZEIT
                FROM game
                WHERE sessionID = \'{session_id}\' AND Spielname = \'{spiel_name}\';"""
        zeit = [i[0] for i in cur.execute(l).fetchall()]
    except:
        print("Fehler beim Ausführen von:" + l)

    colors = ['green','blue','purple','brown','teal', 'yellow', 'black', 'orange']
    plt.bar(user, zeit, color=colors)
    plt.title(spiel_name, fontsize=14)
    plt.xlabel('User', fontsize=14)
    plt.ylabel('Zeit in Sekunden', fontsize=14)
    plt.grid(False)
    plt.savefig(dateiname)