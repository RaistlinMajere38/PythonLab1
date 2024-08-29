import math
from calendar import weekheader

radius=5
area = math.pi * radius ** 2
print("The area of the circle is:", area)

import math
radius = 3
volume = (4/3) * math.pi * radius ** 3
print("The volume of the sphere is:", volume)

import math
a = 3
b = 4
hypotenuse = math.sqrt(a ** 2 + b ** 2)
print("The hypotenuse of the triangle is:", hypotenuse)

name = "Joshua Windle"
length_of_name = len(name)
print("The length of the name is:", length_of_name)

name = "Joshua Windle"
uppercase_name = name.upper()
lowercase_name = name.lower()
print("Uppercase:", uppercase_name)
print("Lowercase:", lowercase_name)
age = 38
height = 5.9
weight = 150
print("Data type of age:",type(age))
print("Data type of height:",type(height))
print("Data type of weight:",type(weight))
weight = 150
height_feet = 5.9
height_inches = height_feet * 12
bmi = (weight / (height_inches ** 2)) * 703
print("The Bod Mass Index (BMI) is:", bmi)

