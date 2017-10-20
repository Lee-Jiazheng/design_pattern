'''
Strategy:
    We generate a serials of 'strategies' that can replace each other.
    We use a factory which can judge result in the server rather than client.
'''

class Cash:
    def acceptCash(self, money):
        pass

# Cash Strategy 1
class CashNormal(Cash):
    def acceptCash(self, money):
        return money

# Cash Strategy 2
class CashRebate(Cash):
    _moneyRebate = 1.0

    def __init__(self, moneyRebate):
        self._moneyRebate = moneyRebate

    @property
    def rebate(self):
        return self._moneyRebate

    @rebate.setter
    def rebate(self, value):
        if 0 <= value <= 1:
            self._moneyRebate = value
        else:
            print("set value illegal!")        

    def acceptCash(self, money):
        return money * self._moneyRebate

# Cash Strategy 3
class CashReturn(Cash):
    moneyCondition = 0.0
    moneyReturn = 0.0
    
    def __init__(self, moneyCondition, moneyReturn):
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn

    def acceptCash(self, money):
        if money >= self.moneyCondition:
            return money - self.moneyReturn
        else:
            return money

class CashContext:
    option = {}
    option["正常收费"] = CashNormal()
    option["满300返100"] = CashReturn(300, 100)
    option["打8折"] = CashRebate(0.8)

    def __init__(self, cash_type):
        if cash_type not in self.option:
            self.real_cash = None
        else:
            self.real_cash = self.option[cash_type]
    
    def GetResult(self, money):
        # we can return max( rebate )
        if self.real_cash is not None:
            return self.real_cash.acceptCash(money)


if __name__ == "__main__":
    cash_context1 = CashContext("打8折")
    print(cash_context1.GetResult(90))
    cash_context2 = CashContext("满300返100")
    print(cash_context2.GetResult(200))
    print(cash_context2.GetResult(500))