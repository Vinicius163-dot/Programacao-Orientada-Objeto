class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1 #[x1,y1]
        self.coor2 = coor2 #[x2,y2]
    
    def distance(self):
        dx = self.coor2[0] - self.coor1[0]
        dy = self.coor2[1] - self.coor1[1]
        return (dx**2 + dy**2) ** 0.5
     
    
    def slope(self):
      # s = y2 - y1/x2 - x1
       dx = self.coor2[1]-self.coor1[1]
       dy = self.coor2[0]-self.coor1[0]
       if dx == 0:
          raise ZeroDivisionError("Slope in a vertical position")
       return dx/dy
coordinate1 = [3,2]
coordinate2 = [8,10]

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())