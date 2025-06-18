#make a base class vehicle
#make two child classes bike and car
#use attributs that can be similar in both class and make some function that are unique and same
 
class Vehicle:
    def __init__(self,color,engcc,name,mileage):
        self.color=color
        self.engcc=engcc
        self.name=name
        self.mileage = mileage
        
    def startengine(self):
        print(f"{self.name} is started")
    def mileage1(self):
        print(f"{self.name} gives {self.mileage} mileage")
        
# vehicle1 = Vehicle("red",200,"yamaha","75kmpl") #comments
# vehicle1.mileage1()
# vehicle1.startengine()

class bike(Vehicle):
    def __init__(self,color,model,gear , engcc, name, mileage):
        super().__init__( color,engcc, name, mileage)
        self.model=model
        self.gear=gear
        
    def what_gear(self):
        print(f"{self.name} has  {self.gear} number of gears ")
    def what_model(self):
        print(f"{self.name}'s model  is {self.model}")
        
class Car(Vehicle):
      def __init__(self, color, seat,engcc, name, mileage):
          super().__init__(color, engcc, name,mileage)  
          self.seat=seat 
        
      def no_seat(self):
          print(f"the car has {self.seat} seat")
             
car1=Car("red",2,1200,"buggati",5)
car1.no_seat()
bike1=bike("black",2021,5,350,"electra","35kmpl")
bike1.what_gear()