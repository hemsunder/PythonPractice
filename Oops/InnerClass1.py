class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()            # Inner class object inside the Outer class

    def show(self):
        print("Student details are ", self.name, self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.ram = 8
            self.proc = 'Intel 8th Gen'

        def show(self):
            print("Student laptop config is ", self.ram, self.proc)


comp1 = student('Hem', 214)
comp2 = student('Durga', 237)

comp1.show()
comp2.show()
comp1.lap.show()                        # We can call inner class method with the help of outer class object
