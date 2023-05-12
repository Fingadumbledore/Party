""" Server logging system """
import os
import time

def clear_log():
    """ clearing log """
    print("f")

def log_server(log, type):
    """ server log""" 
    file_size = os.path.getsize('./Config/log/server.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    log = date + ' [' + type + '] ' + log
    datei = open('./Config/log/server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

        

def chat_log(log,type):
    """ chat log """
    file_size = os.path.getsize('./Config/log/chat.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    log = date + ' [' + type + '] ' + log
    datei = open('./Config/log/chat.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

if __name__ == "__main__":
    print("Use main.py to use program")
