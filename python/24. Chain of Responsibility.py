'''Chain of Responsibility
    In some situiation, some class could not process a request without authorization, and we need to send it to supvisor.
    So for avoiding long method, we use the 'Chain of Responsibility' design pattern.
'''
from abc import abstractmethod
class Manager:
    def __init__(self, name, superior=None):
        self.name = name
        self.superior = superior

    @abstractmethod
    def RequestApplications(self, request):
        pass

class CommonManager(Manager):
    def RequestApplications(self, request):
        if request.num <= 2:
            print(str(request.num) + " is Common Manager process.")
        else:
            self.superior.RequestApplications(request)

class Majordomo(Manager):
    def RequestApplications(self, request):
        if request.num <= 10:
            print(str(request.num) + " is Majordomo process.")
        else:
            self.superior.RequestApplications(request)            

class GeneralManager(Manager):
    def RequestApplications(self, request):
        if request.num <= 50:
            print(str(request.num) + ", General Manager thinks it is OK!")
        else:
            print(str(request.num) + ", General Manager thinks it is a bad thought!")

class Request:
    def __init__(self, num):
        self.num = num

if __name__ == "__main__":
    requests = [Request(1), Request(5), Request(40), Request(100)]
    generalManager = GeneralManager('gen')
    majordomo = Majordomo('maj', generalManager)
    commonManager = CommonManager('com', majordomo)

    # Use the lowest manager
    for request in requests:
        commonManager.RequestApplications(request)
    

