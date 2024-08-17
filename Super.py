from abc import ABC


class Shape(ABC):
    def __init__(self, color: str, is_filled: bool) -> None:
        self.color = color
        self.is_filled = is_filled
        
        
    def discribe(self):
        print(f" it's {self.color} and {'filled' if self.is_filled else 'not filled' }")


class Circle(Shape):
    def __init__(self, color: str, is_filled: bool, radius: float) -> None:
        super().__init__(color, is_filled)
        self.radius = radius
        
    def discribe(self):
        print(f" the area is {3.14 * self.radius**2}")
        super().discribe()


class Triangle(Shape):
    def __init__(self, color: str, is_filled: bool, width: float) -> None:
        super().__init__(color, is_filled)
        self.width = width


class Square(Shape):
    def __init__(self, color:str, is_filled: bool, width: float, height: float) -> None:
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
        
        
circle = Circle("red", True, 5)
triangle = Triangle('blue', False, 1.55)
triangle.discribe()
circle.discribe()
