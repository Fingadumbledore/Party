from argparse import ArgumentParser
import argparse
import os
import shutil
from webserver import main
sessionname = "Test Session"
qinput = " "

def create_session():
    sessionname = input("Session Name: ")
    if not os.path.exists(sessionname): os.makedirs(sessionname)
        
    if not os.path.exists('sammlung'): os.makedirs('sammlung')
       
    main(sessionname)

def load_session():
    sessionname = input("Session Name: ")





def main():
     parser = argparse.ArgumentParser()
     parser.add_argument('--help', help='foo help')
     args = parser.parse_args()

if __name__ == "__main__":
    print("[L]oad Session [C]reate Session")
    qinput = input("Modus: ")
    if (qinput == "L" or qinput == "l"):create_session()

    if (qinput == "C" or qinput == "c"):load_session()
        
    
    
   