'''
Putthipong Phukhansung
633040224-3
'''

def avg_nums():
    sum = 0
    count = 0

    end_input = False
    while not end_input:
        try:
            n = int(input("Enter an integer:"))
            if n < 0:
                break
            sum = sum + n
            count = count + 1
            avg = sum / count
        
        except ValueError:
            print("Please enter an integer")
            exit()
          
    print(f"Average is {avg}")

if __name__ == '__main__':
    avg_nums()
    