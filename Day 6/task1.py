class geometry():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area_rect(self):
        return self.length*self.breadth
        
    def perimeter(self):
        print(f"{2(self.length+self.breadthy)}")
        
area1=geometry(2,3)
print(area1.area_rect())
     
    
  