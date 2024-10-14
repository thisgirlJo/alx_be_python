import math

class  Shape:
    def __init__(self):
        self._p = 0

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)