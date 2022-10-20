from argparse import ArgumentParser
from database import create_database
import os
import shutil
severname = "Test Session"
def create_server():
    create_database()
    





"""
def main():
     parser = ArgumentParser(description='Lan Party Management')
"""

if __name__ == "__main__":
    servername = input("Server Name: ")
    create_server()