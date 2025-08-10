import math
class Shape:
    def area(self):
        """Method to calculate area, must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override area() method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)
