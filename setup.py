from argparse import ArgumentParser
import argparse
import os
import shutil
from webserver import general
sessionname = "Test Session"
qinput = " "

# Session erstellen
def create_session():
    
    if not os.path.exists(sessionname): 
        os.makedirs(sessionname)
        
    if not os.path.exists('sammlung'): 
        os.makedirs('sammlung')   
    general(sessionname)
# Bereits bestehende Session laden
def load_session():
    print("Lade Session")


def main():
     parser = argparse.ArgumentParser()
     parser.add_argument('--help', help='foo help')
     args = parser.parse_args()

if __name__ == "__main__":
    print("[L]oad Session [C]reate Session")
    qinput = input("Modus: ")
    sessionname = input("Session Name: ")
    if (qinput == "L" or qinput == "l"):
        load_session()()

    if (qinput == "C" or qinput == "c"):
        create_session()
        
    
    
   