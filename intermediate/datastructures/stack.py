class Stack:
    def __init__(self):
        self.stack = []
        self.head = -1
    def push(self,value):
        if self.head==-1:
            self.stack=[None]
        else:
            self.stack+=[None]
        self.head+=1
        self.stack[self.head]=value

    def pop(self):
        if self.head==-1:
            return 'empty stack'
        else:
           value = self.stack[self.head]
           self.stack = self.stack[:-1]
           self.head-=1
           return value

stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(5)
stack1.push(17)
print(stack1.stack)


