from abc import ABCMeta , abstractstaticmethod
class IPerson(metaclass= ABCMeta):
    @abstractstaticmethod
    def print_data():
        """ interface Method"""


class SingletonPerson(IPerson):
    __instance = None
    def __init__(self,name):
        if SingletonPerson.__instance != None:
            raise Exception("instance cannot be created as it is already created")
        else:
            self.name = name
            SingletonPerson.__instance = self

    @staticmethod
    def get_instance():
        if SingletonPerson.__instance == None:
            SingletonPerson("Default Name")
        return SingletonPerson.__instance
    @staticmethod
    def print_data():
        print(f'name : {SingletonPerson.__instance.name}')

 
p1 = SingletonPerson("Fahad")
p1.print_data()
p2 = SingletonPerson("ahmed")
p2.print_data()