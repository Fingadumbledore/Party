def clear_log():
    print("f")

def log_server(log, type):
    log = date + ' [' + type + '] ' + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

def chat_log():
    print("chat_log")