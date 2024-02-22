from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

# If subclass is using a abs superclass, need to have all methods
class Laptop(Computer):
    def process(self):
        print("running")

class Programmer:
    def work(self, com):
        print("solving bugs...")
        com.process()


# com = Computer()

com1 = Laptop()
com1.process()

prog1 = Programmer()
prog1.work(com1)