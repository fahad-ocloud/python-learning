import threading
import time

semaphore = threading.BoundedSemaphore(value=5)
def access(thread_number):
    print(f'{thread_number} is trying to access')
    semaphore.acquire()
    print(f'{thread_number} got the access---!!')
    time.sleep(10)
    print(f'{thread_number} is now releasing')
    semaphore.release()


for x in range(1,11):
    t = threading.Thread(target=access , args=(x,))
    t.start()
    time.sleep(1)
