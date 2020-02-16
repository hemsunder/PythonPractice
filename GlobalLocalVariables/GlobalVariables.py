a = 10  # Global Variable


def something():
    a = 15  # Local Variable
    print("inside a value is ", a)


something()
print("Outside a value is ", a)
