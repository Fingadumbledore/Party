import os
import time

def clear_log():
    print("f")

def log_server(log, type):
    file_size = os.path.getsize('server.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    log = date + ' [' + type + '] ' + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

        

def chat_log(log,type):
    file_size = os.path.getsize('chat.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    log = date + ' [' + type + '] ' + log
    datei = open('chat.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()
