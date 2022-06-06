#!/usr/bin/python3

from tkinter import *
import os, sys, sqlite3
from functools import partial

def create_db():
    if os.path.exists("party.db"):
        print("user.db bereits vorhanden")       
    else:
        # Verbindung zur Datenbank erzeugen
        connection = sqlite3.connect("party.db")
        # Datensatz-Cursor erzeugen
        cursor = connection.cursor()
        # Datenbanktabelle erzeugen
        sql = "CREATE TABLE Party(" \
            "usr TEXT, " \
            "usrinfo TEXT)" \
            "Session ID TEXT, " \
            "zeit TEXT, " \
            "SpielName TEXT, " \
            "Spinfo TEXT)"
        cursor.execute(sql)
        # Verbindung beenden
        connection.close()    

def load_session():
    verbunden_status = True

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return


#username label and text entry box


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

   root = Tk()
   lng = Checkbar(root, ['Planer', 'QR-Code', 'User'])
   tgl = Checkbar(root, ['Server','Datenbank'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='abbrechen', command=root.quit).pack(side=RIGHT)
   Button(root, text='start', command=allstates).pack(side=RIGHT)
   root.mainloop()


from tkinter import *

#######
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

def session_window():
	Window.mainloop()
