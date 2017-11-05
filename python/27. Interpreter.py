'''Interpreter:

'''
from abc import ABC, abstractmethod
class Context:
    def __init__(self, c):
        self.c = c

class AbstractExpression(ABC):
    @abstractmethod
    def Interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def Interpret(self, context):
        print("Endpoint interpreter..." + context.c)

class NonTerminalExpression(AbstractExpression):
    def Interpret(self, context):
        print("Non Endpoint interpreter..." + context.c)

if __name__ == "__main__":
    lists = [TerminalExpression(), TerminalExpression(), NonTerminalExpression(), TerminalExpression()]
    context = Context('A')
    for list in lists:
        list.Interpret(context)