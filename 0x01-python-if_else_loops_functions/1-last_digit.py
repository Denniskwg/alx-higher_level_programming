#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
for digit in str(number):
    i = digit
i = int(i)
if number < 0:
    i = -i
if i > 5:
    print("Last digit of {:d} is {} and is greater than 5".format(number, str(i))) 
elif i == 0:
    print("Last digit of {:d} is {} and is 0".format(number, str(i)))
elif i < 6 and i != 0:
    print("Last digit of {:d} is {} and is less than 6 and not 0".format(number, str(i)))
    
