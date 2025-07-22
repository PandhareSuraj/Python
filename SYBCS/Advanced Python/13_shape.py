'''Q.2 Define a class named Shape and its subclass (Square/Circle). The subclass has an init function which takes a an argument (length/redious). Both classes have an area and volume function which can print the area and volume of the shape where Shape's area is 0 by default. '''
import math
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    def volume(self):
        return 0;
    
class circle(shape):
    def __init__(self,r):
        self.r = r
        
    def area(self):
        return math.pi*(self.r**2)
    def volume(self):
        return (4/3)*math.pi*(self.r**3)
    
    
class square(shape):
    def __init__(self,l):
        self.l = l
        
    def area(self):
        return self.l**2
    def volume(self):
        return self.l**3
    
s = square(2)
print("area of Square=",s.area())
print("volume of square=",s.volume())
c = circle(3)
print("area of circle=",c.area())
print("volume of circle=",c.volume())    
