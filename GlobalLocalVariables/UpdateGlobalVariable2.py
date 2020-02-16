a = 10


def something():
    a = 20
    x = globals()['a']
    print("id(x) is ", id(x))
    globals()['a'] = 30
    print("Local variable a value is ", a)
    print("Global variable a value is", globals()['a'])


something()
print("id(a) is", id(a))
print("id(globals()['a']) is", id(globals()['a']))

# Output :
# Local variable a value is  20
# Global variable a value is 30
