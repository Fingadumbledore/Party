from argparse import ArgumentParser
import os
import shutil
sessionname = "Test Session"
dateiname = sessionname + '.py'
def create_session():
    if not os.path.exists(sessionname):
        os.makedirs(sessionname)
        shutil.copy('webserver.py', dateiname)
        shutil.move(dateiname, sessionname)





"""
def main():
     parser = ArgumentParser(description='Lan Party Management')
"""

if __name__ == "__main__":
    sessionname = input("Session Name: ")
    create_session()