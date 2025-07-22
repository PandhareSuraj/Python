'''Q.2 Write a Python Program to Accept and Display students details such as Roll.No, Name, Marks in three subject, using Classes.	'''
class student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        
    def display(self):
        print("roll=",self.roll)
        print("name=",self.name)
        print("marks of three subjects=",self.marks)
        
roll = int(input("Enter the roll no:-"))
name = input("Enter the Name student:-")
marks = []
for i in range(3):
    mark = int(input("Enter the mark:-"))
    marks.append(mark)
    
s = student(roll,name,marks)
s.display()
