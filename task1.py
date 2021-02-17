#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""

#!python3
import math
import time
targetNum = 20
count = 0

while targetNum == 20:
    print(count)
    time.sleep(0.1)
    count = count+2 
    if count > 20:
        break
