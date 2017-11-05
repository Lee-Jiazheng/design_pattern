'''Vistor

'''
from abc import ABC, abstractmethod
class Action(ABC):
    @abstractmethod
    def getManConclusion(self, man):
        pass
    @abstractmethod
    def getWomanConclusion(self, woman):
        pass

class Person(ABC):
    @abstractmethod
    def Accept(self, vistor):
        pass

class Success(Action):
    def getManConclusion(self, man):
        print(man.name + ' ' + self.__class__.__name__)
    def getWomanConclusion(self, woman):
        print(woman.name + ' ' + self.__class__.__name__)

class Failure(Action):
    def getManConclusion(self, man):
        print(man.name + ' ' + self.__class__.__name__)
    def getWomanConclusion(self, woman):
        print(woman.name + ' ' + self.__class__.__name__)

class Man(Person):
    def __init__(self):
        self.name = "Man"
    def Accept(self, vistor):
        vistor.getManConclusion(self)

class Woman(Person):
    def __init__(self):
        self.name = "Woman"

    def Accept(self, vistor):
        vistor.getWomanConclusion(self)

class ObjectStructure:
    def __init__(self, o):
        self.objects = o
    def Display(self, vistor):
        for obj in self.objects:
            obj.Accept(vistor)

if __name__ == "__main__":
    objects = [Man(), Woman()]
    objectStructure = ObjectStructure(objects)
    success = Success()
    failure = Failure()
    objectStructure.Display(success)
    objectStructure.Display(failure)    
    