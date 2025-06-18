# assignment 2:student grade tracker
# build a student class with:

# attributes:name,student id, gpa
# methods:display student info,check if students is pass or not(gpa>2)

class student:
    def __init__(self,name,id,gpa):
        self.name=name
        self.id=id
        self.gpa=gpa
        if(self.gpa<=0):
            print("you cannot have gpa 0")
            exit()
        
    def display(self):
        print(f"{self.name}'s id is {self.id}.The gpa is {self.gpa}")
        
    def check_gpa(self):
        if(self.gpa>2):
            print(f"{self.name} has pass the exam")
        else:
            print(f"{self.name} hasnot pass the exam")
        
    
        