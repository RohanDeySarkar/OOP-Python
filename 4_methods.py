class Student:
    school = "Lawrence"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    
    # Instance Method
    # Accessor (only fetch instance val) (
    def get_m1(self):
        return self.m1
    
    # Mutator (modify the instance val)
    def set_m1(self, val):
        self.m1 = val

    # Class Method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @classmethod
    def setSchool(cls):
        cls.school = "Loyola"
        return cls.school
    
    # Static Method
    @staticmethod
    def info():
        print("This is a static method")

s1 = Student(12, 26, 19)
s2 = Student(87, 66, 54)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())
print(Student.setSchool())

Student.info()