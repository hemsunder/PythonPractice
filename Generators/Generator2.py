

def topten():

    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

t = topten()

for i in t:
    print(i)
