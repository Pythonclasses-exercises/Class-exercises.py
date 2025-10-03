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
import math

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius * radius

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    return 2 * math.pi * radius
