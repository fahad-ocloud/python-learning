class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linklist:

    def __init__(self):
        self.head = None
    
    def insertData(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    def getData(self):
        current = self.head
        while current != None:
            print(current.data)
            current =current.next


l1 = linklist()
l1.insertData(1)
l1.insertData(6)
l1.insertData(7)
l1.insertData(8)
l1.insertData(9)

l1.getData()