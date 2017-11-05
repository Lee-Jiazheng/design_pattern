'''Singleton:
    We can define a variable in a module like 'a = Myclass()', and import this, we will get a singleton 'a'.
    We can also use function decorator.
    We use the '__new__' method.
'''
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  
 
class MyClass(Singleton):  
    a = 1

if __name__ == "__main__":
    one = MyClass()
    two = MyClass()
    '''
    True
    True
    (140299745287528, 140299745287528)
    '''
    print(one == two)
    print(one is two)
    print((id(one), id(two)))