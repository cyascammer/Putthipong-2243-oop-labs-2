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
    i = 0
    round_to_guess = 4
    
    while round_to_guess >= 0:
        try:
            guess_num = int(input("Enter an integer to guess:"))

            if 0 < guess_num <= 10:
                if guess_num < n:
                    print("Try a higher number.")
                    print("You have",round_to_guess,"guesses remaining")
                    i += 1
                    round_to_guess -= 1
                elif guess_num > n:
                    print("Try a lower number.")
                    print("You have",round_to_guess,"guesses remaining")
                    i += 1
                    round_to_guess -= 1

                elif guess_num == n:
                    print("Congrats that you guess the number correctly")
                    break
                else:
                    round_to_guess == 0
                    break
            else:
                raise NameError

        except NameError:
            print("Please enter an integer in the range [1, 10]")                 
        except ValueError:            
            print("Please enter an interger to guess")


if __name__ == '__main__':
    random_number()
    guess_number()

