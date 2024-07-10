class Person:

    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        print(f"Person {self.name} created.")
    def __del__(self):
        print("Person object is deleted!!")
    def __str__(self):
        return "name : {} , age : {}, height : {}".format(self.name,self.age,self.height)
    
class Worker (Person):
    def __init__(self,name,age,height,salary):
        super(Worker,self).__init__(name,age,height)
        self.salary= salary
    def __str__(self):
        text = super(Worker,self).__str__()
        text+= ",salary : {}".format(self.salary)
        return text
    def calc_yearly_salary():
        return salary*12


worker = Worker("fahad",21,6.2,300000)
print(worker.name)
print(worker.age)
print(worker)

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x , self.y - other.y)
    def __str__(self):
        return "X:{}, Y:{}".format(self.x,self.y)

v1 = Vector(2,4)
v2 = Vector(3,6)

print(v1)
print(v2)
v3 = v1+v2

print(v3)
