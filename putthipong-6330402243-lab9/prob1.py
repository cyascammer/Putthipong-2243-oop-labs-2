'''
Putthipong Phukhansung 
633040224-3
'''

import re


def split_str(i):
    for my_info in i:
        result = (re.split(":", my_info))
        result_split = (re.split(" ", result[1]))

        name_str = result[0]
        name_str2 = result_split[0]
        name_str3 = result_split[1]
        name_str4 = result_split[2]
        name_str5 = result_split[3]
        name_str6 = result_split[4]
        id_num = result_split[5]

        result1 = (re.search("[a-zA-Z].+", name_str))
        result2 = (re.search("[a-zA-Z].+", name_str2))
        result3 = (re.search("[a-zA-Z].+", name_str3))
        result4 = (re.search("[a-zA-Z].+", name_str4))
        result5 = (re.search("[a-zA-Z].+", name_str5))
        result6 = (re.search("[a-zA-Z].+", name_str6))
        result7 = (re.search("[0-9].+", id_num))

        print(f"{(result1.group())} {(result6.group())} {(result2.group())} {(result3.group())}"
            f"\n{(result4.group())} {(result5.group())} {(result6.group())} {(result7.group())}")

    
if __name__ == '__main__':
    my_info = ["My name:Manee DeeJai My ID is 642285829"] 
    split_str(my_info)