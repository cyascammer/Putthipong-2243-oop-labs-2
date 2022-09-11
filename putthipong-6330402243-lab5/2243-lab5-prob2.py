'''
Putthipong Phukhansung
633040224-3
'''

import math


def hypotenuse(a, b):

    try:
        x = math.sqrt(pow(a, 2) + pow(b, 2))
        return x

    except Exception:
        pass
    

print(f"hypotenuse(3,4) is {hypotenuse(3.0, 4.0)}")
print(f"hypotenuse('3','4') is {hypotenuse('3','4')}")
print(f"hypotenuse(3, '4.0') is {hypotenuse(3, '4.0')}")
