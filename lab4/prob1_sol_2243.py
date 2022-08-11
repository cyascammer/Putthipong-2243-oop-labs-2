'''
Putthipong Phukhansung
633040224-3
'''

patients = [[70, 1.80], [58, 1.55], [100, 1.90]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

i = 0
for patients in patients:
    weight, height = patients
    bmi = calculate_bmi(weight, height)
    i += 1
    print(f"Patient's BMI is: {bmi:0.02f}")
    