import threading

def function1():
    for x in range(100):
        print("one")
def function2():
    for x in range(100):
        print("two")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()
# function1()
# function2()