'''Iteration:

'''
class IEumerator:
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = -1
        self.element = None
    
    def MoveNext(self):
        pass

    @property
    def current_element(self):
        return self.element

class ConcreteIterator(IEumerator):
    def MoveNext(self):
        ret = None
        self.current += 1
        if self.current < self.aggregate.count:
            self.element = ret = self.aggregate[self.current]
        return ret

class ConcreteIteratorDesc(IEumerator):
    def __init__(self, aggregate):
        super().__init__(aggregate)
        self.current = self.aggregate.count
    
    def MoveNext(self):
        ret = None
        self.current -= 1
        if self.current >= 0:
            self.element = ret = self.aggregate[self.current]
        return ret


class IEnumerable:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, pos):
        return self.items[pos]

    @property
    def count(self):
        return len(self.items)

    def GetEnumerator(self):
        pass

class ConcreteAggregate(IEnumerable):  
    def GetEnumerator(self):
        return ConcreteIterator(self)

class ConcreteAggregateDesc(IEnumerable):  
    def GetEnumerator(self):
        return ConcreteIteratorDesc(self)

if __name__ == "__main__":
    print('*'*15 + 'Ins Iterator')
    concreteAggregate = ConcreteAggregate()
    concreteAggregate.items = "ABCDEFGHIJKLMN"
    enum = concreteAggregate.GetEnumerator()
    while enum.MoveNext() is not None:
        print(enum.current_element, end='\t')
    print('\n' + '*'*15 + 'Desc Iterator')
    concreteAggregate = ConcreteAggregateDesc()
    concreteAggregate.items = "ABCDEFGHIJKLMN"
    enum = concreteAggregate.GetEnumerator()
    while enum.MoveNext() is not None:
        print(enum.current_element, end='\t')
    