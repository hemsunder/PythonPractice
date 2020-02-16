class A:

    def __init__(self):
        print("Class A constructor")

    def method1(self):
        print("Method 1 is working")

    def method2(self):
        print("Method 2 is working")


class B(A):

    def method3(self):
        print("Method 3 is working")

    def method4(self):
        print("Method 4 is working")


b = B()

# Output:
# Class A constructor
