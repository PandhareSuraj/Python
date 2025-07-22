'''Q.2 Python Program to Create a Class in which One Method Accepts a String from the User and Another method Prints it. Define a class named Country which has a method called printNationality. Define subclass named state from Country which has a method called printState . Write a method to print state, country and nationality. '''
class country:
    def __init__(self):
        self.nationality = ""
        
    def inputNationality(self):
        self.nationality = input("Enter the Nationality:-")
        
    def printNationality(self):
        print("Natinality:-",self.nationality)
        
class state(country):
    def __init__(self):
        self.state = ""
        
    def inputState(self):
        self.state = input("Enter the state:-")
        
    def printState(self):
        print("state =",self.state)
        
    def detailPrint(self):
        print(f"Country:-{self.nationality}")
        print(f"Nationality:-{self.nationality}")
        print(f"State:-{self.state}")
        
        
obj = state()

obj.inputNationality()
obj.inputState()

obj.detailPrint()