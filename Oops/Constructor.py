class human:
    def __init__(self):
        self.name = 'hemsunder'
        self.age = 28

    def details(self):
        print("Human details are ", self.name, self.age)

    def update(self):
        self.age = 25

    def compare(self, other):
        if self.age == other.age:
            print("They are same")
        else:
            print("They are not same")


comp1 = human()
comp2 = human()

comp1.name = 'Hem'
comp1.update()

comp1.details()
comp2.details()

comp1.compare(comp2)
