class Figure():

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.add_area() + self.add_area()
        else:
            return ValueError