class Animal:
    def __init__(self,name,ishervibore):
        self.name=name
        self.ishervibore=ishervibore
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def eatsplant(self):
        if(self.ishervibore):
            print(f"{self.name} eats plant")  
        else:
            print(f"{self.name} doesn't eat plant")
class dog(Animal):
    def __init__(self,breed,name,ishervibore):
        super().__init__(name,ishervibore)
        self.breed=breed
    def make_sound(self):
        print(f"{self.name} is barking")
    def print_breed(self):
        print(f"{self.name} is {self.breed} dog")
    def fetch_bone(self):
        print(f"{self.name} fetch bone")
        
class cat(Animal):
    def __init__(self,breed,name,ishervibore):
        super().__init__(name,ishervibore)
        self.breed=breed
    def make_sound(self):
            print(f"{self.name} is saying meow")
    def print_breed(self):
            print(f"{self.name} is {self.breed}cat")
        
cat1=cat("kale","Tom",True)
    
cat1.make_sound()
cat1.eatsplant()
cat1.print_breed()
cat1.sleep()

    
dog1=dog("german shephard","Max" ,False)
dog1.sleep()
dog1.make_sound()
dog1.fetch_bone()
        
        