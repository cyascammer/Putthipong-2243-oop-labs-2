'''
Putthipong Phukhansung
633040224-3
'''

import logging


input_logging = False

while not input_logging:
    try:
        n1 = int(input("Enter n1:"))
        n2 = int(input("Enter n2:"))
        result = n1 / n2
        print(f"The result is {result}")

        logging.basicConfig(level=logging.DEBUG,
                            filename='logs-2243.txt',
                            filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s')

        logging.debug(f"n = {n1}")
        logging.debug(f"n = {n2}")
        break

    except NameError:
        print(" is not giving error code ")
  