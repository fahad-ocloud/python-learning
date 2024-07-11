from abc import ABCMeta , abstractstaticmethod

class IPerson(metaclass= ABCMeta):
    @abstractstaticmethod
    def person_method(self):
        """ interface Method"""


class Person(IPerson):

    def person_method(self):
        print("I am a Person")
    

class Proxy_person(IPerson):

    def __init__(self):
        self.person = Person()
    
    def person_method(self):
        print("I am proxy function")
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = Proxy_person()
p2.person_method()