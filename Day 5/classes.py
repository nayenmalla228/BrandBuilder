# create a class to input users number and print multiplication table and factorial

class ABC:
    def __init__(self,num):
        self.num= num
        
    def multiplication(self):
      
      for i in range(1,11):
       mult = num1 * i
       print(mult)
        


        
    def factorial(self):
      fact = 1
      for i in range(1, num1+1):
        fact*= i
      print(fact)
      
        
    
num1 = int(input("enter a number"))
    
newnum1=ABC(num1)
newnum1.factorial()
newnum1.multiplication()