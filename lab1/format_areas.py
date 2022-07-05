'''
Puttthipong Phukhansung
633040224-3
'''


import math


info = ("radius", "height", "surface_area")


print(f"{info[0]} {info[1]:>6} {info[2]:>12}")


for i in range (1, 11):    
    radius = i
    height = i * 2
    surface_area = (2 * math.pi * radius *(radius + height))

    print(f"{radius:6} {height*2:6} {surface_area:12.2f}")
