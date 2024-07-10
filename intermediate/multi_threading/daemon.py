import threading 
import time 

path = "daemon_text.txt"
text= ""

def readFile():
    global path, text
    while True:
        with open("text.txt","r") as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for x in range(10):
        print(text)
        time.sleep(1)    


t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()