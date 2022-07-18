from argparse import ArgumentParser
import os
import shutil
from webserver import main
sessionname = "Test Session"

def create_session():
    if not os.path.exists(sessionname):
        os.makedirs(sessionname)
        






"""
def main():
     parser = ArgumentParser(description='Lan Party Management')
"""

if __name__ == "__main__":
    sessionname = input("Session Name: ")
    create_session()
    main(sessionname)