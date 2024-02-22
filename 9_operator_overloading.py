# a = '5'
# b = '6'

# print(a + b)

# a + b --behind scene--> str.__add__(a, b)

# print(str.__add__(a, b))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2 

    # Overload __add__
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        
        s3 = Student(m1, m2)
        return s3
    
        # return m1 + m2
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True 
        else:
            return False
        
    def __str__(self):
        return f'{self.m1} {self.m2}'


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m1, s3.m2)

if s1 > s2:
    print("s1 win")
else:
    print("s2 win")


a = 9
print(a)
print(a.__str__()) # same as above

print(s1)
print(s1.__str__()) # same as above