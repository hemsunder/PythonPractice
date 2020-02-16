def div(a, b):
    print(a / b)


def smartdiv(func):
    def inner(x, y):
        if x < y:
            x, y = y, x
            return func(x, y)

    return inner


div = smartdiv(div)
div(5, 10)

# Output: 2.0
# A Function which is used to add some extra feature or modify the logic of existing function is called as "Decorator".
