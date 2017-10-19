'''
Observer:
    It is very hard for me and cost about one hour for this code.
'''
from functools import reduce
class StackObserver:
    def __init__(self, name, sub):
        self.name = name
        self.subject = sub

    def CloseStackMarket(self):
        print("%s, %s close the stock and go to work," % (self.subject.state, self.name))

# although the construct method is same as 'StackObserver'
# in the real world, they maybe different entities completely
class NBAObserver:
    def __init__(self, name, sub):
        self.name = name
        self.subject = sub

    def CloseNBALive(self):
        print("%s, %s close the NBA and go to work," % (self.subject.state, self.name))
        
class Subject:
    def __init__(self, name):
        self.name = name
    state = ""
    # 'Notify' is a method used to notify observers actually
    def Notify(self):
        raise NotImplementedError

class Delegate:
    def __init__(self, delegates = []):
        self.delegates = delegates

    def __iadd__(self, other):
        self.delegates.append(other)
        return Delegate(self.delegates)
    def __add__(self, other):
        self.delegates.append(other)
    def __radd__(self, other):
        self.delegates.append(other)

    def __getitem__(self, pos):
        return self.delegates[pos]        

    def __repr__(self):
        # print all the method name
        return reduce(lambda x, y: x+' '+y.__name__, self.delegates, "")

class Boss(Subject):
    Update = Delegate()
    def __init__(self, name):
        super().__init__(name)
        self.state = "%s is back" % name
    
    def Notify(self):
        for update in self.Update:
            update()


if __name__ == "__main__":
    boss = Boss("lee_jiazh")
    stockObserver = StackObserver("Wright", boss)
    nbaObserver = NBAObserver("Thrown", boss)
    boss.Update += stockObserver.CloseStackMarket
    boss.Update += nbaObserver.CloseNBALive
    print(boss.Update)
    boss.Notify()

