class A:
    def __init__(self, color = "Blue"):
        self.__color = color
    def set_color(self, color):
        self._color = color
    def show_color(self):
        return self.__color
obj1 = A()
obj1._color = 'Red'
print(obj1.show_color())
obj1.A_color = 'Red'
print(obj1.show_color())
