# Parent class (super class)
class A:
    def __init__(self):
        print("init A")

    def feature1(self):
        print("Feature 1")
    
    def feature2(self):
        print("Feature 2")

# Child class (sub class)
class B(A):
    def __init__(self):
        # Access parent's init
        super().__init__()
        print("init B")

    def feature3(self):
        print("Feature 3")
    
    def feature4(self):
        print("Feature 4")

# When A, B separate class!
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         # will take A init only not B
#         # LEFT -> RIGHT (Method Resolution Order (MRO))
#         print("init C")
        

# a1 = A()

# If no innit in B, takes A'init
# For getting noth A/B init in B, use seuper in B init
b1 = B()

####################################################################################################
# Parent class
class A:
   def __init__(self, a_name):
       self.a_name = a_name
   
# Child class
class B(A):
    def __init__(self, b_name, a_name):
        self.b_name = b_name
        # invoke constructor of class A
        super().__init__(a_name)
        # Alternative
        # A.__init__(self, a_name)
    
        # If just want to use like A.a_name instead of self.a_name
        # A.a_name = a_name 
    
    def display_names(self):
        print("A name : ", self.a_name)
        print("B name : ", self.b_name)


#  Driver code
b = B('child', 'parent')
b.display_names()
