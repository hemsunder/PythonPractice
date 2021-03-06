class A:

    def __init__(self):
        print("Class A constructor")

    def method1(self):
        print("Method 1 is working")

    def method2(self):
        print("Method 2 is working")


class B:

    def __init__(self):
        print("Class B constructor")

    def method3(self):
        print("Method 3 is working")

    def method4(self):
        print("Method 4 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("Class C constructor")


c = C()

# Output:
# Class A constructor
# Class C constructor
