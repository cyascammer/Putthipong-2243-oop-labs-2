'''
Putthipong Phukhansung
633040224-3
'''

class Numbers:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def add(self):       
        a = self.x + self.y
        return a
                
    def display_factors(i):
        if i % 6:
            factor1 = (i + 1) / 2
            factor2 = factor1 - 1
            return(f"Factors of {i} is {factor2:.0f} and {factor2:.0f}")
        else:
            factor1 = i / 2
            return(f"Factors of {i} is {factor1} and {factor1}")

    def is_valid_divisor(i):
        if i == 0:
            return(f"{i} is not a valid divisor")
        else:
            return(f"{i} is a valid divisor")
            

if __name__ == '__main__':
    print(f"2 + 3 is {Numbers(2, 3).add()}")
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))