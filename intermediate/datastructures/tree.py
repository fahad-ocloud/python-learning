from queue import Queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insertintotree(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                current = queue.get()
                if current.right is None:
                    current.right = new_node
                    break
                elif current.right is not None:
                    queue.put(current.right)
                if current.left is None:
                    current.right = new_node
                    break
                elif current.left is not None:
                    queue.put(current.right)

    def get_Tree(self):
        queue = Queue()
        queue.put(self.root)  
        while not queue.empty():
            current  = queue.get()
            print(current.data)
            if current.right is not None:
                queue.put(current.right)
            if current.left is not None:
                queue.put(current.left)


t1 = Tree()
t1.insertintotree(1)
t1.insertintotree(2)
t1.insertintotree(3)
t1.insertintotree(4)
t1.insertintotree(7)
t1.insertintotree(8)
t1.insertintotree(19)

t1.get_Tree()