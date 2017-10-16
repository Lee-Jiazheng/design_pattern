'''
Static Factory Method:
    It is a way that supports alternative function and convinent to extend.
    It provides with a base class and a factory class to instantiate a kind of subclass.
'''

class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.num1 + self.num2

class OperationSub(Operation):
    def GetResult(self):
        return self.num1 - self.num2

class OperationMul(Operation):
    def GetResult(self):
        return self.num1 * self.num2

class OperationDiv(Operation):
    def GetResult(self):
        try:
            return self.num1 / self.num2
        except:
            print("Divided by zero.")
            return 0

class OperationUndef(Operation):
    def GetResult(self):
        print("Not defined operator.")
        return 0

operation = {}
operation["+"] = OperationAdd()
operation["-"] = OperationSub()
operation["*"] = OperationMul()
operation["/"] = OperationDiv()

class OperationFactory():
    
    @staticmethod
    def createOperate(op ):
        if op in operation:
            return operation[op]
        else:
            return OperationUndef()

if __name__ == "__main__":
    op = input("operator: ")
    num1 = input("num1: ")
    num2 = input("num2: ")
    oper = OperationFactory.createOperate(op)
    oper.num1 = int(num1)
    oper.num2 = int(num2)
    print(oper.GetResult())