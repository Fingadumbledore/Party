from argparse import ArgumentParser
import argparse
import os
import shutil
from webserver import general
sessionname = " "
qinput = " "
typ = " "


# Session erstellen
def create_session():
    
    if not os.path.exists(sessionname): 
        os.makedirs(sessionname)
        
    if not os.path.exists('sammlung'): 
        os.makedirs('sammlung')   
    general(sessionname, typ)
# Bereits bestehende Session laden

def main():
     parser = argparse.ArgumentParser()
     parser.add_argument('--help', help='foo help')
     args = parser.parse_args()

if __name__ == "__main__":
    print("[T]emp Session [C]reate Session")
    qinput = input("Modus: ")
    sessionname = input("Session Name: ")
    if (qinput == "T" or qinput == "t"):
        typ = "t"
        general(sessionname, typ)

    if (qinput == "C" or qinput == "c"):
        typ = "n"
        create_session()
        
    
    
   