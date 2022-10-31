from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        return None

    @abstractmethod
    def calculate_perimeter(self):
        return None


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        area = self.__width * self.__height
        return area

    def calculate_perimeter(self):
        perimeter = 2 * ( self.__width + self.__height)
        return perimeter


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        area = self.__radius * self.__radius * pi
        return area

    def calculate_perimeter(self):
        perimeter = 2 * self.__radius * pi
        return perimeter


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
