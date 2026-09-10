class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calc_area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 3)

print("Area of the rectangle:", rectangle1.calc_area())