from abc import ABC,abstractmethod
class Calculater(ABC):
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def multi(self,a,b):
        print(a*b)
    @abstractmethod
    def div(self):
        pass
class junior(Calculater):
    def div(self):
        pass
obj=junior()
obj.add(2,3)
obj.multi(2,3)
    