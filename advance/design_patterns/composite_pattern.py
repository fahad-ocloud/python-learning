from abc import ABCMeta , abstractstaticmethod,abstractmethod

class IDepartment(metaclass= ABCMeta):
    @abstractmethod
    def __init__(self):
        """ implement in child class"""
    @abstractstaticmethod
    def print_department():
        """ implement in child class"""


class Accounting(IDepartment):
    def __init__(self,employees):
        self.employees = employees
    def print_department(self):
        print(f"Accounting Department : {self.employees}")
class Development(IDepartment):
    def __init__(self,employees):
        self.employees = employees
    def print_department(self):
        print(f"Development Department : {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_dep = []
    
    def add(self,dept):
        self.sub_dep.append(dept)
        self.employees+=dept.employees
    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employeees: {self.base_employees}")
        for dept in self.sub_dep:
            dept.print_department()
        print(f"Total Employeees: {self.employees}")

d1 = Accounting(100)
d2 = Development(300)

p1 = ParentDepartment(1000)

p1.add(d1)
p1.add(d2)

p1.print_department()