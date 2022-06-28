#Putthipong Phukhansung
#633040224-3


num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
sum = float(num1 + num2)
result1 = (f"{num1} + {num2} = {sum}")
print(result1)


with open('numbers.txt', 'w') as numbers:
    numbers.write(result1)
    print("Writing to file numbers.txt")

with open('numbers.txt', 'r') as numbers:
    data = numbers.read()
    print("Reading from file numbers.txt")
    print(data)
