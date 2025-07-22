'''Q.2 Python Program to Create a Class which Performs Basic Calculator Operations'''class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print("sum=",self.a+self.b)
    def sub(self):
        print("sub=",self.a-self.b)
    def mul(self):
        print("mul=",self.a*self.b)
    def div(self):
        print("div=",self.a/self.b)
        
a = int(input("Enter the value of a:-"))
b = int(input("Enter the value of b:-"))
c = calculator(a,b)
c.add()
c.sub()
c.mul()
c.div()
