from abc import ABCMeta,abstractmethod

class Iperson(metaclass=ABCMeta):
    @abstractmethod
    def get_data():
        """Abstract method"""

class PersonSingleton(Iperson):
    __instance = None

    def __init__(self,name,age):
        if(PersonSingleton.__instance == None):
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
        else:
            raise Exception("Not more than once !!!")

    @staticmethod
    def get_instance():
        if(PersonSingleton.__instance == None):
            PersonSingleton("Human",18)
        return PersonSingleton.__instance

    @staticmethod
    def get_data():
        print("instance method is :",PersonSingleton.__instance.age)

p = PersonSingleton("Ram", 30)
#p1 = PersonSingleton("Raj", 30)
p.get_data()
p2 = PersonSingleton.get_instance()
p2.get_data()