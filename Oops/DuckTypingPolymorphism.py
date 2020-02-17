class Pycharm:
    def execute(self):
        print("Compiles")
        print("Run Programme")


class MyownEditor:
    def execute(self):
        print("Spell check")
        print("Code convention")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = Pycharm()
ide = MyownEditor()
lap = Laptop()
lap.code(ide)
