'''Adapter
    It is a good design pattern, but the best way is that we think all things when design the system.
    It supports a serials interface to coordinate two different interfaces' classes.
'''
from abc import abstractmethod
class Player:
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def defense(self):
        pass

class Forwards(Player):
    def attack(self):
        print("Forward %s attack." % self.name)
    def defense(self):
        print("Forward %s defense." % self.name)

'''and other classes'''
class Center(Player):
    pass
class Guards(Player):
    pass

# Note: it has the same interface as Player class, so it is Player's subclass
class Translator(Player):
    def __init__(self, name):
        super().__init__(name)  
        self.Center = ForeignCenter(name)
    def attack(self):
        self.Center.foreign_attack()
    def defense(self):
        self.Center.foreign_defense()

class ForeignCenter:
    def __init__(self, name):
        self.name = name
    def foreign_attack(self):
        print("中锋 %s 进攻！" % self.name)
    def foreign_defense(self):
        print("中锋 %s 防守！" % self.name)

if __name__ == "__main__":
    mike = Forwards("Mike")
    mike.attack()
    mike.defense()
    YaoMing = Translator("YaoMing")
    YaoMing.attack()
    YaoMing.defense()