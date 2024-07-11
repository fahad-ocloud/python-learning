class Person:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value

    @staticmethod
    def staticMethod():
        print("I'm static")
    

p1 =Person("fahad",23,"Male")
Person.staticMethod()
p1.Name = "Ali"
print(p1.Name)