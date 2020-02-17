class marks:

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            x = a + b + c
        elif a is not None and b is not None:
            x = a + b
        else:
            x = a
        print(x)


m = marks()
m.sum(10, 20, 30)
m.sum(10, 20)
m.sum(10)
