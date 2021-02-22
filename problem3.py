#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
import math
import time


# nth is current number
# ais the previous number
# b is last number
a=0
b=1
nth=a+b
while True: 
    print( nth,end=" ",flush=True)
    nth = a + b
    a = b
    b = nth
    if nth > 100:
        break