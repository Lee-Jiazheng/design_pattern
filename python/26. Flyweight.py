'''Flyweight
    
'''
from abc import ABC, abstractmethod
class Chess:
    def __init__(self, pos):
        self.pos = pos
        
class Website(ABC):
    @abstractmethod
    def Use(self, user):
        pass

class ConcreteWebsite(Website):
    def __init__(self, name):
        self.name = name
    def Use(self, user):
        print("Chess:" + self.name + " Pos: " + user.pos)

class WebsiteFactory:
    def __init__(self):
        self.flyweights = {}
    def get(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteWebsite(key)
        return self.flyweights.get(key)
    def count(self):
        return len(self.flyweights)

if __name__ == "__main__":
    f = WebsiteFactory()
    fx = f.get("white")
    user = Chess('(1, 1)')
    fx.Use(user)
    fy = f.get("white")
    fy.Use(Chess('(2, 3)'))
    f1 = f.get("black")
    f1.Use(Chess('(3, 4)'))
    f2 = f.get("black")
    f2.Use(Chess('(9, 9)'))