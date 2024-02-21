class Car:
    # Class variable
    wheels = 4

    def __init__(self):
        # Instance varible
        self.mil = 10
        self.com = "AUDI"

c1 = Car()
c2 = Car()

c1.mil = 8

# only updates for c1
# c1.wheels = 5

Car.wheels = 5

# Won't work
# Car.mil = 68

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)