'''
Builder:
    The process of building is stable, so we implement the abstract method.
    In the 'Director' class, we assemble serials of components to a whold entity. 
'''
from abc import ABC, abstractmethod
class PersonBuilder(ABC):
    @abstractmethod
    def BuildHead(self):
        pass
    @abstractmethod
    def BuildBody(self):
        pass
    @abstractmethod
    def BuildLimb(self):
        pass
    @abstractmethod
    def BuildLeg(self):
        pass

class PersonThinBuilder(PersonBuilder):
    def BuildHead(self):
        print("Thin Head")
    def BuildBody(self):
        print("Thin Body")    
    def BuildLimb(self):
        print("Thin Limb") 
    def BuildLeg(self):
        print("Thin Leg")    

class PersonFatBuilder(PersonBuilder):
    def BuildHead(self):
        print("Fat Head")
    def BuildBody(self):
        print("Fat Body")    
    def BuildLimb(self):
        print("Fat Limb") 
    def BuildLeg(self):
        print("Fat Leg")    

# It is used to direct the process of building...
class Director:
    def Build(self, builder):
        builder.BuildHead()
        builder.BuildBody()
        builder.BuildLimb()
        builder.BuildLeg()

if __name__ == "__main__":
    director = Director()
    print("-"*10 + "Thin Person Building...")
    director.Build(PersonThinBuilder())
    print("-"*10 + "Fat  Person Building...")
    director.Build(PersonFatBuilder())