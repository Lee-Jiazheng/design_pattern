'''
Decorator:
    The assembled order is not important.
'''

# it stands for the concrete component.
class Person:
    name = ''

    def __init__(self, name):
        self.name = name
    
    def Show(self):
        print("the decoration is %s" % self.name)
    
class Finery(Person):
    component = None
    def __init__(self):
        pass
    
    def Decorate(self, component):
        self.component = component
    
    def Show(self):
        if self.component is not None:
            self.component.Show()
    
class TShirts(Finery):
    def Show(self):
        print("T-shirt ", end='')
        super().Show()
    
class BigTrouser(Finery):
    def Show(self):
        print("Big-Trouser ", end='')
        super().Show()

class Sneaker(Finery):
    def Show(self):
        print("Sneaker ", end='')
        super().Show()

if __name__ == "__main__":
    person = Person("Lee")
    print("-------------")
    tshirts = TShirts()
    bigtrouser = BigTrouser()
    sneaker = Sneaker()
    tshirts.Decorate(person)
    bigtrouser.Decorate(tshirts)
    sneaker.Decorate(bigtrouser)
    sneaker.Show()
