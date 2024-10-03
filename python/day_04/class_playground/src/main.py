class Shape:
    def area(self):
        print("This is the area function!")
        
class Square(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def perimeter(self): ...
    
shape = Shape()
square = Square(
    width =2,
    height=2
)

square.area()
square.perimeter() 