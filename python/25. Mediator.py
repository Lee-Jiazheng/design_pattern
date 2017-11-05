'''Mediator
    Multiple classes have 'm-m' relationship, so we build a 'Mediator' class.
'''
from abc import ABC, abstractmethod
class UnitedState(ABC):
    @abstractmethod
    def Declare(self, message, colleague):
        pass

class Country(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

class China(Country):
    def Declare(self, message):
        self.mediator.Declare(message, self)
    def GetMessage(self, message):
        print("the China get message: " + message)

class USA(Country):
    def Declare(self, message):
        self.mediator.Declare(message, self)
    def GetMessage(self, message):
        print("the USA get message: " + message)

class Iraq(Country):
    def Declare(self, message):
        self.mediator.Declare(message, self)
    def GetMessage(self, message):
        print("the Iraq get message: " + message)

class ConcreteUnitedState(UnitedState):
    def __init__(self):
        self.colleagues = []
    def append(self, colleague):
        self.colleagues.append(colleague)

    def Declare(self, message, c):
        for colleague in self.colleagues:
            if colleague is not c:
                colleague.GetMessage(message)

if __name__ == "__main__":
    UNSC = ConcreteUnitedState()
    usa = USA(UNSC)
    iraq = Iraq(UNSC)
    china = China(UNSC)
    UNSC.append(usa)
    UNSC.append(iraq)
    UNSC.append(china)

    usa.Declare('I am the USA')
    iraq.Declare('I am the Iraq')
    