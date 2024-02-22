# Method Overloading -> 2 func same name

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a == None:
            a = 0
        if b == None:
            b = 0
        if c == None:
            c = 0
        s = a + b + c
        return s


s1 = Student(58, 69)

print(s1.sum(9))


# Method overriding
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1 = A()
a1.show()

b1 = B()
# First check if show() is in B, else use show() from A
b1.show()