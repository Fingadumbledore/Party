from client import build_window
from argparse import ArgumentParser
from database import creat_stand_db as sdb
from database import create_user_db as udb
import os, sys
from client import terminal 
from pathlib import Path
import subprocess

def main():
    parser = ArgumentParser(description='Party Controll Center')
    parser.add_argument('-g', '--gui', action='store_true', help='Open GUI')
    parser.add_argument('-t', '--terminal', dest='terminal', nargs='+', help='help')
  
    args = parser.parse_args()
    if args.gui:
        build_window()
    elif args.terminal:
       terminal()
        
    else:
        parser.print_help()
          

if __name__ == "__main__":
    exit(main())