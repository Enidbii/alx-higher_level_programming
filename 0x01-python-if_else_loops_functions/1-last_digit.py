#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if number > 0:
    if int(last_digit) > 5:
        print("Last digit of {} is {} and is greater than 5".format
              (number, last_digit))
    elif int(last_digit) < 6 and int(last_digit) != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format
              (number, last_digit))
else:
    print("Last_digit of {} is -{} and is less than 6 and not 0".format
          (number, last_digit))
