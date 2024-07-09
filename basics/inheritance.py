class Person:
    def speak(self):
        print(f"{self.name} is speaking")


class Employee(Person):
    def __init__(self, name):
        self.name =name
    def working_in_factory(self):
        print("working in factory")

class Student(Person):
    def study(self):
        print("studying")


student = Employee("Fahad")
student.speak()