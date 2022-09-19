'''
Putthipong Phukhansung
633040224-3
'''


def get_float(arg):
    while True:
        try:
            num = input(f"Please enter the {arg} operand ('q' to quit):")
            if num == "q" or num == "Q":
                return num
            num = float(num)
            if num != float(num):
                raise Exception
            return num
        except:
            print("Please enter a valid decimal number")


def robust_calculator():
    global n1
    global n2

    while True:
        n1 = get_float("first")
        if n1 == "q" or n1 == "Q":
            break
        n2 = get_float("second")
        if n2 == "q" or n2 == "Q":
            break
        
        calculator()


def calculator():
    list_operator = ["+","-","*","/"," "]

    try:
        input_operator = input("Enter an operator (+,-,*,/):")
        if input_operator == "+" or input_operator == "":
            result = n1 + n2
            input_operator = "+"
        elif input_operator == "-":
            result = n1 - n2                
        elif input_operator == "*":
            result = n1 * n2                
        elif input_operator == "/":
            result = n1 / n2
        else:
            print("Operation must be +, -, * or /.")
              
        if input_operator in list_operator:
            math = input("Enter out format (float, int):")
            if math == "float" or math == "":
                result = float(result)
                print(f"{n1} {input_operator} {n2} = {result}")
            if math == "int":
                result = int(result)
                print(f"{n1} {input_operator} {n2} = {result}")

    except ZeroDivisionError:
        print("Cannot divide by zero \nWe cannot perform your requested calculation")

        robust_calculator()

if __name__ == "__main__":
    robust_calculator()
