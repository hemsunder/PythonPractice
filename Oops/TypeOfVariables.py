class Car:

    wheels = 4  # Class Variable or Static Variable

    def __init__(self):
        self.mil = 10                       # Instance Variable
        self.companyname = 'BMW'            # Instance Variable


comp1 = Car()
comp2 = Car()

Car.wheels = 5

print(comp1.mil, comp1.companyname, comp1.wheels)
print(comp2.mil, comp2.companyname, comp2.wheels)
