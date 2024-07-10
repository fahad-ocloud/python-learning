import gc
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
    

person1 = Person("fahad", 21, 6.2)
print(person1.name)
print(person1.age)
print(person1.height)
print(person1)
# gc.collect()
