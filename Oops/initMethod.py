class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Human details are ", self.name, self.age)


obj1 = human('hemsunder', 28)
obj2 = human('Durga', 27)



obj1.details()
obj2.details()
