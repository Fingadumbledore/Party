from tkinter import *
import tkinter as tk
from tkinter import messagebox
from server import server
import threading
import pyqrcode
import os, sys
from pathlib import Path
import subprocess
import time
import qrcode
from session import session
from tkinter import filedialog 
#https://www.python-kurs.eu/tkinter_entry_widgets.php
server_on = FALSE
session_status = FALSE
verbunden_status = FALSE
sessionload = FALSE
verlauf = open('verlauf.txt', 'r')
tverlauf = verlauf.read()
ip = "http://192.168.178.56:8000"


    

  
    

def create_session():
    print("erstelle session")
    qr = qrcode.make(ip)
    qr.save('session.png')
    subprocess.run(["./session.sh" ])
    return
    


def load_session():
    print("Lade Session")
    
    verbunden_status = "yes"
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
        
    
    
 
def action_get_erstellen_dialog():
    if verbunden_status:
        t_text = "Session erstellen"
        messagebox.showinfo(message=t_text, title = "erstellen")
        create_session()
        #server()
    else:
        q_text = "Du bist bereits in einer Session willst du diese Verlassen?"
        messagebox.showinfo(message=q_text, title = "Warnung")
        

def action_get_verlauf_dialog():
    #get_verlauf()
    t_text = tverlauf
    print("öffne Verlauf")
    messagebox.showinfo(message=t_text, title = "Verlauf")
    #server()
    
        
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: fingadumbledore\n\
Copyright: 2022\n\
Version: 0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")

def build_window():       
    fenster = tk.Tk()
    fenster.title("Party Controll ")
    fenster.geometry("450x400")
    fenster.tk.call('wm', 'iconphoto', fenster._w, tk.PhotoImage(file='party.png'))



    if server_on :
        info_text = Label(fenster, text = "Guten Tag")
        info_text.pack()
    else:
        info_text = Label(fenster, text = "Guten Tag\n\
        Bitte verbinde dich mit einer Session oder erstelle eine.")
        info_text.pack()
    
            

    # Menüleiste erstellen 
    menuleiste = Menu(fenster)
   

    # Menü Datei und Help erstellen
    datei_menu = Menu(menuleiste, tearoff=0)
    help_menu = Menu(menuleiste, tearoff=0)

    # Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
    # Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
    
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    datei_menu.add_command(label="Verlauf", command=action_get_verlauf_dialog)
    
    #datei_menu.add_separator() # Fügt eine Trennlinie hinzu
    if verbunden_status:
     datei_menu.add_command(label="Erstellen", command=action_get_erstellen_dialog)
     datei_menu.add_command(label="Laden", command=load_session)
     datei_menu.add_command(label="Exit", command=fenster.quit)
    else: 
        info_text = Label(fenster, text = "Sie befinden sich im Moment noch in einer Session")

    help_menu.add_command(label="Info!", command=action_get_info_dialog)

    # Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
    # "Drop-Down-Menü" hinzu
    menuleiste.add_cascade(label="Session", menu=datei_menu)
    menuleiste.add_cascade(label="Help", menu=help_menu)

    # Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
    fenster.config(menu=menuleiste)    
        

    fenster.mainloop()


def terminal():
    subprocess.run(["./session.sh" ])