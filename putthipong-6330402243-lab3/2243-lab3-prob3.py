'''
Putthipong Phukhansung
633040224-3
'''

def check():
    
    string = str(input("Enter a string:"))
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

    lenString = [each for each in string if each in string]
    check_vowel = [each for each in string if each in vowels]

    print(f"chare are {lenString}")


    if check_vowel == []:
        print(f"There is no vowel in entered string {string}")
    else:
        print(f"The entered string is {string} and the resuit of convert a vowel to uppercase is")
        for i in range(len(check_vowel)):
            check_vowel[i] = check_vowel[i].upper()
        print(check_vowel)


if __name__ == '__main__':
    check()
