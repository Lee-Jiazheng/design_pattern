'''
Facade:
    This pattern hides interior members, only supports the interface calling. 
    We don't need to concern about what in it like the relationship of foundations and stocks.
'''

class Stock:
    def __init__(self, name):
        self.name = name

class Fund:
    stock_name = ["stock1", "stock2", "stock3"]
    def __init__(self):
        self.stocks = [ Stock(name) for name in self.stock_name]
    
    def GetFund1(self):
        print(self.stock_name[0])
        print(self.stock_name[1])
    
    def GetFund2(self):
        print(self.stock_name[0])
        print(self.stock_name[2])

if __name__ == "__main__":
    fund = Fund()
    print("-"*15 + 'fund 1 buying')
    fund.GetFund1()
    print("-"*15 + 'fund 2 buying')
    fund.GetFund2()