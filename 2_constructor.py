class Computer:
    def __init__(self):
        self.name = "Rohan"
        self.age = 24
    
    def update(self):
        self.age = 50

    def compare(self, other):
        if self.age == other.age:
            return True 
        else:
            return False

c1 = Computer()
c2 = Computer()

# c1 becomes "self"
if c1.compare(c2):
    print("They r same")
else:
    print("They r diff")


# Heap memory (evry time create a obj -> allocated to new space)
# Size of an object -> depends on no. of variables & size of each variable
# Who allocates size of obj -> constructor
# print(id(c1))
# print(id(c2))

c1.name = "Sam"
c2.age = "32"

c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)