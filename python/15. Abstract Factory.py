'''
Abstract Factory:
    Multiply operators and multiply factories.
'''
from abc import ABC, abstractmethod

# Actually it should get from a configuration files, so I found a generator replace it.
def get_database():
    for database in ["SqlServer", "Access"]:
        yield database
gen = get_database()

class DataAccess:
    db = None
    @staticmethod
    def create_user():
        class_name = DataAccess.db + "User"
        return eval(class_name+'()')

    @staticmethod
    def create_department():
        class_name = DataAccess.db + "Department"
        return eval(class_name+'()')
    
class IUser(ABC):
    @abstractmethod
    def get_user(self, id):
        pass

class SqlServerUser(IUser):
    def get_user(self, id):
        print("Sql Server get a user that id is " + str(id))

class AccessUser(IUser):
    def get_user(self, id):
        print("Access get a user that id is " + str(id))      

class IDepartment(ABC):
    @abstractmethod
    def insert_department(self, name):
        pass

class SqlServerDepartment(IDepartment):
    def insert_department(self, name):
        print("Sql Server insert %s department" % name)

class AccessDepartment(IDepartment):
    def insert_department(self, name):
        print("Access insert %s department" % name)        

# If the process is stable, we can use "Builder" pattern.
def repeat():
    DataAccess.db = next(gen)
    user = DataAccess.create_user()
    user.get_user(1)
    depart = DataAccess.create_department()
    depart.insert_department("tencent ")


if __name__ == "__main__":
    repeat()
    repeat()