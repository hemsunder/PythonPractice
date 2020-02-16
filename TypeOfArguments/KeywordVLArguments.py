# Keyword Variable length arguments


def person(name, **data):
    print(name)
    print(data)

    for i, j in data.items():
        print(i, j)


person('hemsunder', age=28, city='hyderabad', mob=8309048464)
