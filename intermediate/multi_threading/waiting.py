import threading

def hello():
    for x in range(10):
        print("hello")
    
t1 = threading.Thread(target=hello)
t1.start()
t1.join()
print("hekkoecbvc cjcj")