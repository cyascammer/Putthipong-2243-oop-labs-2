'''
Putthipong Phukhansung 
633040224-3
'''

import sys


try:
    operator1 = sys.argv[1]
    operand2 = float(sys.argv[2])
    operand3 = float(sys.argv[3])

    if operator1 == "q" or operator1[0] == "Q":
        print("Program quits...")
        exit()
    elif operator1[0] == "+":
        result_plus = operand2 + operand3
        print(f"{operand2} {operator1} {operand3} is {result_plus}")
    elif operator1[0] == "-":
        result_minus = operand2 - operand3
        print(f"{operand2} {operator1} {operand3} is {result_minus}")
    elif operator1[0] == "*":
        result_multiply = operand2 * operand3
        print(f"{operand2} {operator1} {operand3} is {result_multiply}")
    elif operator1[0] == "/":
        result_divide = operand2 / operand3
        print(f"{operand2} {operator1} {operand3} is {result_divide}")
    else:
        raise IndexError

except ZeroDivisionError:
    print(f"{operand2} cannot be divided by {operand3}")

except IndexError:
    print(f"Usage: {sys.argv[0]} <operator1> <operand2> <operand3>")

except ValueError:
    print("Operands are invalid. They are not numbers")