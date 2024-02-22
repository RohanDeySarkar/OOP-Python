# Polymorphism

# walks like a duck, quacks like a duck, swims like a duck -> it is a duck

class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class Vscode:
    def execute(self):
        print("syntax check")
        print("spell check")
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        ide.execute()

# If there's an object which has execute (not concerned about what class object it is)
# ide = Pycharm()      
ide = Vscode()

lap1 = Laptop()
lap1.code(ide)
