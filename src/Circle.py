import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        self.name = "Круг Михаил"
        self.r = r
        self.d = r * 2


    def area(self):
        return self.r * math.pi

    def perimeter(self):
        return self.r * math.pi * 2


