'''
Template:
    The abstract method impelements in its subclass, but we use its interface in template code.
    Importance: We deferring algorithmic details to child classes.
'''
from abc import ABC, abstractmethod
class TestPaper(ABC):
    # it is a template that descript the flow of operation.
    def TestQuestion1(self):
        print("Q: What is your name?")
        print("A: %s" % self.Answer1())
    
    def TestQuestion2(self):
        print("Q: How old are you?")
        print("A: %s" % self.Answer2())

    @abstractmethod
    def Answer1(self):
        pass
    @abstractmethod
    def Answer2(self):
        pass
    
class TestPaperA(TestPaper):
    def Answer1(self):
        return "lee"
    def Answer2(self):
        return 20

class TestPaperB(TestPaper):
    def Answer1(self):
        return "thrown"
    def Answer2(self):
        return 66

if __name__ == "__main__":
    studentA = TestPaperA()
    studentA.TestQuestion1()
    studentA.TestQuestion2()
    studentB = TestPaperB()
    studentB.TestQuestion1()
    studentB.TestQuestion2()