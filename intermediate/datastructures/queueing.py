from queue import Queue

q = Queue()
numbers = [10, 20, 30, 40, 50, 60]
for number in numbers:
    q.put(number)

while not q.empty():
    print(q.get())
