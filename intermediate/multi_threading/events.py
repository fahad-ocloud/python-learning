import threading

event = threading.Event()
def event_triggering():
    print("event is waiting to trigger... ")
    event.wait()
    print("event is triggered")

t1 = threading.Thread(target=event_triggering)
t1.start()

value  = input("Fo you want to trigger the event (y/n)")
if value =='y':
    event.set()