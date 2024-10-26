import math

class Shape:
    def __init__(self, len, breg):
        self.len = len
        self.breg = breg
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius** 2)