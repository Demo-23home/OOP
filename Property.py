class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            return "the width should be greater than 0"
        
        

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            return "the height should be greater than 0"

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
        
        

rect = Rectangle(3, 4)
rect.height = 10
rect.width = 20
print(rect.height, rect.width)
del rect.width
