'''
Putthipong Phukhansung 
633040224-3
'''

import csv


with open("numbers.csv", "w", newline="") as fw:
    write = csv.writer(fw)
    write.writerow([2, 4, 6])
    write.writerow([3, 7, 5])
    write.writerow([8, 9, 7])

with open("numbers.csv", "r") as i:
    with open("numbers2.csv", "w", newline="") as fw2:
        rows = csv.reader(i)
        write2 = csv.writer(fw2)
        for row in rows:
            row[0], row[2] = row[2], row[0]
            number = (float(row[0]) + float(row[1]) + float(row[2])) / len(row)
            row.append(number)
            write2.writerow(row)

with open("numbers2.csv", "r") as j:
    lines = csv.reader(j)
    for line in lines :
        print(line)