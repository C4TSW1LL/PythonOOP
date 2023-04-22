import math
from src.Figure import Figure

class Triangle(Figure):

    def __init__(self, a, b, c):
        if (a < b + c) and (b < a + c) and (c < a + b):
            self.hp = (a + b + c) / 2
            self.name = "Треугольник"
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError

    def area(self):
        return int(math.sqrt(self.hp * (self.hp - self.a) * (self.hp - self.b) * (self.hp - self.c)))

    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(12,13,14)
print(triangle.area())