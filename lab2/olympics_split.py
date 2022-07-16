'''
Puttthipong Phukhansung
633040224-3
'''

olympics2020_str = "Badminton: Thailand vs. Great Britain" \
    "Table Tennis: Thailand vs. Japan"

badminton, country, tennis = olympics2020_str.split(":")



if __name__ == '__main__':
    print("For some Olympics 2020 games of thai ahtletes:")

    sport1 = country.replace("Table Tennis","")
    print(f"For {badminton}, the game is between{sport1}")
    sport2 = country.replace("Thailand vs. Great Britain","")
    print(f"For{sport2}, the game is between{tennis}")