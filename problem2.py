#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

import math
import time

count =int(input("Please enter a numbrer"))
a=count
while True:
    print(count, end =" ", flush=True)
    time.sleep(0.1)
    count = a+count
    if count > math.pow(a,12):
       break