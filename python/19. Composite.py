'''
Composite:
    When the requirment reflects the structure of the part and the whole level, or you would like to ignore the differences of 'composite objects'(branch company) and 'single objects'(some company department).
    We will unify all the objects to only one structure(class definition, i.e. abstract company).
'''

class Company:
    name = ""

    def __init__(self, name):
        self.name = name

    def Add(self, company):
        pass
    
    def Remove(self, company):
        pass

    def Display(self, depth):
        pass
    
    def LineOfDuty(self):
        pass

# the subcompany definition
# Warning: if the children defined out of '__init__', all the objects will use the same children, and it will lead to an fetal error.
class ConcreteCompany(Company):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def Add(self, company):
        self.children.append(company)
    
    def Remove(self, company):
        self.children.remove(company)
    
    def Display(self, depth):
        print('-'*depth + self.name)
        for child in self.children:
            child.Display(depth + 2)
    
    def LineOfDuty(self):
        for child in self.children:
            child.LineOfDuty() 

class HRDepartment(Company):
    # it is the leap with no child component
    def Display(self, depth):
        print('-'*depth + self.name)

    def LineOfDuty(self):
        print("I'm HRing.")

class FinanceDepartment(Company):
    # it is the leap with no child component
    def Display(self, depth):
        print('-'*depth + self.name)

    def LineOfDuty(self):
        print("I'm Financing.")

if __name__ == "__main__":
    root = ConcreteCompany("Beijing head office")
    root.Add(HRDepartment("head office HR"))
    changchun = ConcreteCompany("Changchun branch office")
    root.Add(changchun)
    changchun.Add(HRDepartment("Changchun HR"))
    changchun.Add(FinanceDepartment("Changchun Finance"))

    print("-"*15)
    root.Display(1)
    print("-"*15)
    root.LineOfDuty()
    
            