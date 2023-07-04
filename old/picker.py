""" game picker for party games """
import shutil
import os
import sqlite3
import matplotlib.pyplot as plt


def dbcon(sqlstring):
    """ connect to database and execute sqlstring """
    print ("test")
    try:
        con = sqlite3.connect("party.db")
        cur = con.cursor()
        cur.execute(sqlstring)
    except sqlite3.Error as sqlite_error:
        raise Exception(f"error: {sqlite_error}")


def game(name: str):
    """ does sql stuff with game name """
    print(name)
    sql_query = ""
    match name:
        case "nfsu2":
            sql_query = "nfsu2"
        case "anno1602":
            sql_query = "anno1602"
        case "tmbr":
            sql_query = "tmbr"
        case _:
            sql_query = "no game found"


    dbcon(sql_query)

def picker(gamefile, session_id, spieler_id):
    """ game picker """
    datei = open(gamefile, 'a')
    game(check)
    if not os.path.exists(session_id):
        os.makedirs(session_id)
    shutil.move(gamefile, session_id)


if __name__ == "__main__":
    print("Use main.py to use program")
