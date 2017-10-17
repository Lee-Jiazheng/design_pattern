'''
Factory Method:
    In the Simple Factory, the judgement is in the server, you will 1.add a class definition 2.alter the 'switch' statement 3.alter the client code.
    However, the Factory Method provides a way that only add a Factory class and class definition.
    Therefore, we obey the rule 'be open for extension, but closed for modification(i.e. not modify the class definition like the 'switch' statement).'
'''
from abc import ABC, abstractclassmethod

class LeiFeng:
    def Sweep(self):
        print("Sweep.")
    def Wash(self):
        print("Wash.")
    def BuyRice(self):
        print("Buy Rice.")

class Undergraduate(LeiFeng):
    pass

class Volunteer(LeiFeng):
    pass

class IFactory(ABC):
    @abstractclassmethod
    def CreateLeifeng(self):
        pass

class UndergraduateFactory(IFactory):
    def CreateLeifeng(self):
        return Undergraduate()

class VolunteerFactory(IFactory):
    def CreateLeifeng(self):
        return Volunteer()

if __name__ == "__main__":
    # if it is other objects, you need to alter just one code.
    factory = UndergraduateFactory()
    student = factory.CreateLeifeng()
    student.BuyRice()
    student.Sweep()
    student.Wash()