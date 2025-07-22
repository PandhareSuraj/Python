import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    def volume(self):
        return 0
    
class Circle(Shape):
    def __init__(self,r):
       # super().__init__()
        self.r = r
        
    def area(self):
        print(f"area={math.pi*(self.r**2)}")
        
    def volume(self):
        print(f"Volume={(4/3*math.pi*(self.r**3))}")
        
        
class square(Shape):
    def __init__(self,l):
       # super().__init__()
        self.l = l   
        
    def area(self):
        print("area=",self.l**2)
        
    def volume(self):
        print("Volume=",self.l**3)
        
        
        
s = square(2)
s.area()
s.volume()
c = Circle(2)
c.area()
c.volume()