from tkinter import *
from tkinter import messagebox
from server import server
import threading
import pyqrcode
#https://www.python-kurs.eu/tkinter_entry_widgets.php
server_on = "no"
fields = ('Session name', 'Anzahl Teilnehmer', 'Anwendung')

def button_action():
        print("Ich wurde über das Menü ausgeführt.")

def action_get_erstellen_dialog():
    t_text = "Session erstellen"
    messagebox.showinfo(message=t_text, title = "erstellen")
    #server()

def action_get_verlauf_dialog():
    t_text = "Verlauf"
    messagebox.showinfo(message=t_text, title = "Verlauf")
    #server()


def action_get_verbinden_dialog():
    f_text = "Mit Session verbinden"
    messagebox.showinfo(message=f_text, title = "verbinden")

    
        
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: fingadumbledore\n\
Date: 2022\n\
Version: 0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")

def build_window():       
    fenster = Tk()
    fenster.title("Party Controll")
    fenster.geometry("450x400")



    info_text = Label(fenster, text = "Guten Tag\n\
    Bitte verbinde dich mit einer Session oder erstelle eine.")
    info_text.pack()
    if server_on == "yes":
        info_text = Label(fenster, text = "Server ist bereit\n\
    Bitte verbinde dich endweder mit localhost, oder mit der ip deines rechners.")
    info_text.pack()
            

    # Menüleiste erstellen 
    menuleiste = Menu(fenster)

    # Menü Datei und Help erstellen
    datei_menu = Menu(menuleiste, tearoff=0)
    help_menu = Menu(menuleiste, tearoff=0)

    # Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
    # Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
    datei_menu.add_command(label="Erstellen", command=action_get_erstellen_dialog)
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    datei_menu.add_command(label="Verbinden", command=action_get_verbinden_dialog)
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    datei_menu.add_command(label="Verlauf", command=action_get_verlauf_dialog)
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    datei_menu.add_command(label="Exit", command=fenster.quit)

    help_menu.add_command(label="Info!", command=action_get_info_dialog)

    # Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
    # "Drop-Down-Menü" hinzu
    menuleiste.add_cascade(label="Session", menu=datei_menu)
    menuleiste.add_cascade(label="Help", menu=help_menu)

    # Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
    fenster.config(menu=menuleiste)    
        

    fenster.mainloop()