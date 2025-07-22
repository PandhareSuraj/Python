'''Q.2 Write a Python Program to Accept and Display employee details such as No, Name, Salary using Classes.	'''class employee:
    def __init__(self,no,name,salary):
        self.no = no
        self.name = name
        self.salary = salary
        
    def display(self):
        print("no=",self.no)
        print("name=",self.name)
        print("salary=",self.salary)
        
no = int(input("ENter the no="));
name = input("ENter the name:-");
salary = int(input("Enter the salary:-"))
s = employee(no,name,salary)
s.display()
