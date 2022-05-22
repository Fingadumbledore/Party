from tkinter import *
from tkinter import messagebox
from server import server
import threading
import pyqrcode
import subprocess


def close_session():
	print("test")
	

def run_server():
	#subprocess.run([server() ])
	return

def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: fingadumbledore\n\
Copyright: 2022\n\
Version: 0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")

def session():
	
	fenster = Tk()
	fenster.title("Session")
	fenster.geometry("450x400")

	info_text = Label(fenster, text = "Session")
	info_text.pack()



	# Menüleiste erstellen 
	menuleiste = Menu(fenster)

	# Menü Datei und Help erstellen
	datei_menu = Menu(menuleiste, tearoff=0)
	help_menu = Menu(menuleiste, tearoff=0)

	# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
	# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
	datei_menu.add_command(label="Server", command=run_server())
	datei_menu.add_separator() # Fügt eine Trennlinie hinzu
	datei_menu.add_command(label="Exit", command=close_session())

	help_menu.add_command(label="Info!", command=action_get_info_dialog)

	# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
	# "Drop-Down-Menü" hinzu
	menuleiste.add_cascade(label="Session", menu=datei_menu)
	menuleiste.add_cascade(label="Help", menu=help_menu)

	# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
	fenster.config(menu=menuleiste)    

	
	fenster.mainloop()
	