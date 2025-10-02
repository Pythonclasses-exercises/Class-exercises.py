import math
class Circle:
   def __init__(self, radius):
      self.radius = radius 
   def area(self):
      return math.pi * self.radius **2
   def circumference(self):
      return 2 * math.pi * self.radius
   
Question_1 = Circle(22)

print(Question_1.area())
print(Question_1.circumference())