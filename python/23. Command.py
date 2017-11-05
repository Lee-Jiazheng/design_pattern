'''Command:

'''
from abc import ABC, abstractmethod
import time
class Barbecuer:
    def BakeMutton(self):
        print("Baking Mutton...")
    def BakeChickenWing(self):
        print("Baking Chicken Wing...")

class Command:
    def __init__(self, receiver=None):
        self.receiver = receiver
    @abstractmethod
    def Execute(self):
        pass

class BakeMuttonCommand(Command):
    def Execute(self):
        self.receiver.BakeMutton()

class BakeChickenWingCommand(Command):
    def Execute(self):
        self.receiver.BakeChickenWing()
    
class Waiter:
    def __init__(self):
        self.commands = []
    
    def SetOrder(self, command):
        if isinstance(command, BakeChickenWingCommand):
            print("No chicken!")
        else:
            self.commands.append(command)
            # this is a log
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '   Add Command ' + str(command)) 

    def CancelOrder(self, command):
        self.commands.remove(command)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '   Remove Command ' + str(command)) 
        
    def Notify(self):
        for command in self.commands:
            command.Execute()

if __name__ == "__main__":
    boy = Barbecuer()
    bakeMuttonCommand1 = BakeMuttonCommand(boy)
    bakeMuttonCommand2 = BakeMuttonCommand(boy)
    bakeChickenWingCommand = BakeChickenWingCommand(boy)
    girl = Waiter()
    
    girl.SetOrder(bakeMuttonCommand1)
    girl.SetOrder(bakeMuttonCommand2)
    girl.SetOrder(bakeChickenWingCommand)
    girl.CancelOrder(bakeMuttonCommand2)
    girl.Notify()

    