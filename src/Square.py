from src.Figure import Figure

class Square(Figure):

    def __init__(self, a):
        self.a = a
        self.name = "Квадрат"

    def area(self):
        return self.a * self.a

    def perineter(self):
        return self.a * 4

square = Square(10)
print(square.area())
print(square.perineter())
