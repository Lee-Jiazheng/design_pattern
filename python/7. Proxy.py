'''
Proxy:
    It provides a proxy, and hides the real object. Hence, we can apply it to 'access control', 'replace some large object'(by proxying it a temporary small object).
'''

from abc import ABC, abstractmethod

# interface: it contains all the manipulations of proxy and real-object.
# it should inherite 'ABC' and some method mark as '@abstractmethod'
class IGiveGift(ABC):
    # its subclass must implement this method.
    @abstractmethod
    def GiveDolls(self):
        pass
    
    def GiveFlowers(self):
        raise NotImplementedError

    def GiveChocolate(self):
        raise NotImplementedError

class SchoolGirl():
    __name = ''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

# it presents a 'real-object'.
class Pursuit(IGiveGift):
    # he want to access schoolGirl indirectly
    def __init__(self, girl):
        self.schoolGirl = girl

    def GiveDolls(self):
        print("%s, give you the dolls." % self.schoolGirl.name)

    def GiveFlowers(self):
        print("%s, give you the flowers." % self.schoolGirl.name)

    def GiveChocolate(self):
        print("%s, give you the chocolate." % self.schoolGirl.name)
    
# it is the proxy...
class Proxy(IGiveGift):
    def __init__(self, girl):
        self.pursuit = Pursuit(girl)
    
    def GiveDolls(self):
        self.pursuit.GiveDolls()

    def GiveFlowers(self):
        self.pursuit.GiveFlowers()

    def GiveChocolate(self):        
        self.pursuit.GiveChocolate()

if __name__ == "__main__":
    girl = SchoolGirl()
    girl.name = "run_ze"

    proxy = Proxy(girl)
    proxy.GiveChocolate()
    proxy.GiveDolls()
    proxy.GiveFlowers()

    # we can't instantiate this abstract class 'IGiveGift' because of its abstract methods...
    # test = IGiveGift()