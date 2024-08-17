from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, raduis: float) -> None:
        self.raduis = raduis

    def area(self) -> float:
        area = self.raduis**2 * 3.14
        return area


class Triangle(Shape):
    def __init__(self, base:float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        area = 0.5 * self.base * self.height
        return area


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        area = self.side * self.side
        return area
    
    
class Pizza(Circle):
    def __init__(self, raduis: float, topping:str) -> None:
        super().__init__(raduis)
        self.topping = topping
        

    
    
shapes = [Circle(4), Triangle(5, 7), Square(6), Pizza(15, "Cheese") ]
for shape in shapes:
    area = shape.area()
    print( f"{area} cm2")