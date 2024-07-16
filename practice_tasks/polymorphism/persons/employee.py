from .parent import IPerson
class Employee(IPerson):
    def __init__(self,name,age, salary):
        super().__init__(name,age,salary)
    
    def work(self):
        print(f"{self.name} works in Factory")