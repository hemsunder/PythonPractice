class A:

    def phone(self):
        print("Nokia 1100")


class B(A):
    def phone(self):
        print("Motorola")


a = B()
a.phone()
