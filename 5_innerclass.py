class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    # Innerclass
    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Rohan", 2)
s2 = Student("Naruto", 3)

s1.show()
s1.Laptop().show()

# lap1 = s1.lap
# lap2 = s1.lap

lap1 = Student.Laptop()
lap1.show()