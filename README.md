# Programação Orientada a Objetos

Nesse repositório coloco em prática a programação orientada a objetos para criar projetos que exigem a elaboração de cálculos e fórmulas.

## Projeto 1 - Cálculo de distância e inclinação de 2 pontos com coordenadas

Nesse projeto são dadas 2 coordenadas (a primeira e a segunda). O código coleta essas 2 coordenadas e realiza as fórmulas necessárias para encontrar a distância e a inclinação da linha traçada a partir delas.

Demonstração do código 👇

```python
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
```



## Projeto 2 - Cálculo do volume e área da superficie de um cilindro

Nesse projeto utilizo a mesma lógica do projeto da linha porém com as formulas corretas para o calculo de ambos os parâmetros solicitados

```python
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
```

Ambos os projetos poderiam ser simplificados através do uso da biblioteca ja inserida no python, que seria ```import math ```, porém decidi optar por estruturar as formulas de forma manual para ir se acostumando cada vez mais com a indentação do python




