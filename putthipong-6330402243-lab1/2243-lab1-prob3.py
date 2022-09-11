'''
Puttthipong Phukhansung
633040224-3
'''


import math


input_radius = float(input("Enter radius:"))

if input_radius > 0:
    input_height = float(input("Enter height:"))

    if input_height > 0:
        surface_area = ((2 * math.pi * input_radius) * input_height) + ((math.pi * input_radius ** 2) * 2)
        print(f"The surface area of a cyclinder with radius \n{input_radius} and height {input_height} is {surface_area}")
        

    else:
        print("Please enter a positive number for height")

else: 
    print("Please enter a positive number for radius")
