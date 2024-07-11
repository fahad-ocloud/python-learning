from abc import ABC,abstractmethod

class IPerson(ABC):
    @abstractmethod
    def person_method(self):
        """ interface Method"""
        pass
class Employee(IPerson):
    def __init__(self):
        self.name= "I am a employee"
    def person_method(self):
        print("I'm Employee")
class Teacher(IPerson):
    def __init__(self):
        self.name= "i am a Teacher"
    def person_method(self):
        print("I'm Teacher")

class PersonFactory:
    @staticmethod
    def build_person(type):
        if type == "employee":
            return Employee()
        if type == "teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    x = input ("What type of object you want to build : ")
    person = PersonFactory.build_person(x)
    person.person_method()