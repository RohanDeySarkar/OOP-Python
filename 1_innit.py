class Computer:
    # Attributes -> Variables
    # Behaviour -> Methods(Function)

    # Initiator (constructor)
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram 
        
    def config(self):
        print("Config is", self.cpu, self.ram)

# com1 is an object of computer
com1 = Computer('i5', 16)
com2  = Computer('i7', 8)

# print(type(com1))

# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()