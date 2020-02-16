class A:
    def method1(self):
        print("Method 1 is working")

    def method2(self):
        print("Method 2 is working")


class B(A):
    def method3(self):
        print("Method 3 is working")

    def method4(self):
        print("Method 4 is working")


class C(B):                                     # Multi Level Inheritance
    def method5(self):
        print("Method 5 is working")


a = A()
b = B()
c = C()

c.method1()
c.method2()
c.method3()
c.method4()
c.method5()

