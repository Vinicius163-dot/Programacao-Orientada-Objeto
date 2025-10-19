class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        pi = 3.14159
        paramethers = (self.radius **2)* pi
        final_result = paramethers * self.height
        print(final_result)

    
    def surface_area(self):
        pi = 3.14159  
        base = (self.radius ** 2)
        height_cylinder = self.radius * self.height
        semifinal_sum = base * 2 + height_cylinder * 2 
        final_sum =  semifinal_sum * pi
        print(final_sum)  


c = Cylinder(height=2,radius=3)


print(c.volume())
print(c.surface_area())