from abc import ABC, abstractmethod
class IPerson(ABC):
    def __init__(self,name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    @abstractmethod
    def work(self):
        """ interface methods"""