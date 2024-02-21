# Parent class (super class)
class A:
    def feature1(self):
        print("Feature 1")
    
    def feature2(self):
        print("Feature 2")

# Child class (sub class)
class B(A):
    def feature3(self):
        print("Feature 3")
    
    def feature4(self):
        print("Feature 4")

# Multiple inheritance
# class C(A, B):...

a1 = A()

a1.feature1()

b1 = B()
b1.feature2()