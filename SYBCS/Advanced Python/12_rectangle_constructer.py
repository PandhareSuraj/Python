'''Q.2 Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area and volume.'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

 
    def volume(self, height=1):
        return self.length * self.width * height


rect = Rectangle(10, 5)


print("Area of the rectangle:", rect.area())

print("Volume of the rectangle:", rect.volume(3))
