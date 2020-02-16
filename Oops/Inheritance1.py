class A:
    def method1(self):
        print("Method 1 is working")

    def method2(self):
        print("Method 2 is working")


class B(A):                                 # Single Level Inheritance
    def method3(self):
        print("Method 3 is working")

    def method4(self):
        print("Method 4 is working")


a = A()
b = B()
b.method1()
b.method2()
b.method3()
b.method4()
