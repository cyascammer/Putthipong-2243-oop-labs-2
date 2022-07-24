'''
Putthipong Phukhansung
633040224-3
'''

import random



def random_number():  
    global n 
    min_num = 1
    max_num = 10
    n = random.randint(min_num, max_num)
    return n

def guess_number():
    guess_num = int(input("Enter an integer to guess:"))
    i = 0
    round_to_guess = 4

    while round_to_guess >= 0:
        try:

            if guess_num < n:
                print("Try a higher number.")
                print("You have",round_to_guess,"guesses remaining")
                guess_num = int(input("Enter an integer to guess:"))
                i += 1
                round_to_guess -= 1
            elif guess_num > n:
                print("Try a lower number.")
                print("You have",round_to_guess,"guesses remaining")
                guess_num = int(input("Enter an integer to guess:"))
                i += 1
                round_to_guess -= 1

            elif guess_num <= 0 or guess_num > 10 :
                print(f"Please enter an integer in th range [1, 10]")
            else:
                break
            
                       
        except ValueError:            
            print("please enter an interger to guess")
        

      

    if guess_num == n:
            print("Congrats that you guess the number correctly")


if __name__ == '__main__':
    random_number()
    guess_number()

