'''Bridge
    We can compose some component with "aggregation" relationship.
    So there will not be much more subclass-es.
'''
from abc import ABC, abstractmethod
class HandSetSoft(ABC):
    @abstractmethod
    def Run(self):
        pass

class HandSetGame(HandSetSoft):
    def Run(self):
        print("Runnings mobile game...")

class HandSetContract(HandSetSoft):
    def Run(self):
        print("Running mobile contract...")

class HandSetBrand(ABC):
    def __init__(self, soft):
        self.soft = soft
    @abstractmethod
    def Run(self):
        pass

class HandSetBrandM(HandSetBrand):
    def Run(self):
        self.soft.Run()

class HandSetBrandN(HandSetBrand):
    def Run(self):
        self.soft.Run()

# Add Brand
class HandSetBrandS(HandSetBrand):
    def Run(self):
        self.soft.Run()

# Add Software
class HandSetMP3(HandSetSoft):
    def Run(self):
        print("Running player 3...")
        
if __name__ == "__main__":
    hm = HandSetBrandM(HandSetGame())
    hm.Run()
    hm.soft = HandSetContract()
    hm.Run()
    