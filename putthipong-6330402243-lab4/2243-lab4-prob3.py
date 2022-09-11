'''
Putthipong Phukhansung
633040224-3
'''

while True:
    try:
        
        yesterday = int(input("Enter the number of new infected Covid19 cases for yesterday:"))
        while yesterday < 0:
            print("You can only enter a non-negative integer. \nStay healthy!")            
            yesterday = int(input("Enter the number of new infected Covid19 cases for yesterday:"))
            break
        
        today = int(input("Stay healthy! \nEnter the number of new infected Covid19 cases for today:"))
        while today < 0:
            print("You can only enter a non-negative integer. \nStay healthy!")            
            today = int(input("Enter the number of new infected Covid19 cases for today:"))
            break

        percent = ((today - yesterday) / yesterday) * 100
        print(f"Stay healthy! \nThe difference of the number of new infected case is {percent:.2f}%")
        break


    except ValueError:
        print("Plese enter a valid integer \nStay healthy!")
        