'''
Puttthipong Phukhansung
633040224-3
'''

student_id = int(input("Enter your student ID:"))


while True:
    try:
        midterm_score = float(input("Enter the student's midterm exam mark (0-100):"))
        if midterm_score <= 100 and midterm_score >= 0:
            break
        elif midterm_score <= 0 or midterm_score >= 100:
            print("Enter a score in rage[0,100]")
    except ValueError:
        print("Enter a score as a decimal number.")

midterm = (midterm_score * 40/100)

while True:
    try:
        final_score = float(input("Enter the student's final exam mark (0-100):"))
        if final_score  <= 100 and final_score  >= 0:
            break
        elif final_score  <= 0 or final_score >= 100:
            print("Enter a score in rage[0,100]")
    except ValueError:
        print("Enter a score as a decimal number.")


finalterm = (final_score * 60/100)
totalscore = finalterm + midterm


if totalscore >= 80 and totalscore <= 100:
    getgrade = 'A'
elif totalscore >= 70 and totalscore <= 80:
    getgrade = 'B'
elif totalscore >= 60 and totalscore <= 70:
    getgrade = 'C'
elif totalscore >= 50 and totalscore <= 60:
    getgrade = 'D'
else:
    getgrade = 'F'


print(f'Student ID {student_id} has the total mark as {totalscore} and has grade as {getgrade}')
