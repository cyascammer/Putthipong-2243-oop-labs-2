'''
Putthipong Phukhansung
633040224-3
'''

ADD, SUB, MUL, DIV = range(4)

def flexible_calculator(operator, output_format, *number):
    result = 0

    if operator == ADD:
        for a in number:
            result += a
    elif operator == SUB:
        result = number[0]
        for a in number:
            result -= number[a + 1]
    elif operator == MUL:
        result = 1
        for a in number:
            result *= a
    elif operator == DIV:
        result = number[0]
        for a in number:
            result /= a
        result *= number[0]

    if output_format == float:
        return float(result)
    elif output_format == int:
        return int(result)


if __name__ == '__main__':
    try:
        print(f"flexible_calculator(ADD, int, 1) = {flexible_calculator(ADD, int, 1)}")
        print(f"flexible_calculator(ADD, int, 1, 2) = {flexible_calculator(ADD, int, 1, 2)}")
        print(f"flexible_calculator(ADD, int, 1, 2, 3, 4) = {flexible_calculator(ADD, int, 1, 2, 3, 4)}")
        print(f"flexible_calculator(MUL, int, 2, 3, 4) = {flexible_calculator(MUL, int, 2, 3, 4)}")
        print(f"flexible_calculator(DIV, float, 10, 5, 2) = {flexible_calculator(DIV, float, 10, 5, 2)}")
        print(f"flexible_calculator(DIV, float, 5, 0) = {flexible_calculator(DIV, float, 5, 0)}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

