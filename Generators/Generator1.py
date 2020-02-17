

def sum():

    yield 1            # Instead of return keyword we user yield in generators
    yield 2
    yield 3


s = sum()
print(s.__next__())
print(s.__next__())


for i in s:
    print(i)