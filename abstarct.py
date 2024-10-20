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
------------------------------------------------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")   


# Attempting to create an instance of the abstract class will raise an error
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract method speak

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
