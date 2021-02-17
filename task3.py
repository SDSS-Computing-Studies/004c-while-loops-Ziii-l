#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
number ="-10000"

while number != int(number):
    number = input("please enter number")
    number =float(number)
    even= ((number%2)==0)
    if number != int(number) :
        print("That is not an even integer")

print("That is an even integer")