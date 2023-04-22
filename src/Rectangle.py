from src.Figure import Figure

class Rectangle(Figure):

    def __init__(self, a, b):
        if a != 0 and b != 0:
            self.a, self.b = a, b
            self.name = "Прямоугольник"
        else:
            raise ValueError
    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a*2 + self.b*2

# rectangle = Rectangle(10, 15)
# print(rectangle.area())
# print(rectangle.perimeter())