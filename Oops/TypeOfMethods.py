class Student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def marks(self):                                        # Instance Method
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod                                            # Class Method
    def getschool(cls):
        print(cls.school)

    @staticmethod                                           # Static Method
    def info():
        print("Details are available")


comp1 = Student(36, 45, 96)
comp2 = Student(39, 86, 75)

print(comp1.marks())
print(comp2.marks())
Student.getschool()