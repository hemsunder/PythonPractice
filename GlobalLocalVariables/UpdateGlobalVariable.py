a = 10


def something():
    global a
    a = 20
    print("a value is ", a)


something()

# Output : a value is  20
