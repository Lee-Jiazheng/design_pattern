'''
Prototype:
    The main problem is 'deepcopy' in Clone method.
'''
import copy
class Resume:
    name = None
    sex = None
    age = None
    workExperience = None

    def __init__(self, name, sex, age, timeArea, company):
        self.name = name
        self.sex = sex
        self.age = age
        self.workExperience = WorkExperience(timeArea, company)
    
    def Display(self):
        print("%s %s %s, Woke Experience: %s %s" % (self.name, self.sex, self.age, self.workExperience.timeArea, self.workExperience.company)) 

    def Clone(self):
        return copy.deepcopy(self)

class WorkExperience:
    timeArea = None
    company = None
    def __init__(self, timeArea, company):
        self.timeArea = timeArea
        self.company = company

if __name__ == "__main__":
    a = Resume('li', 'male', '17', '2019', 'tencent')
    b = a.Clone()
    b.sex = 'female'
    b.workExperience.timeArea = '2018'
    a.Display()
    b.Display()