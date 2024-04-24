#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
x = int(input("Enter a number less than 10> "))

for i in range(1, x+1):
    if x < 10:
        print(x * "*")
    else: 
        print(f"The number you have entered, {x}, is not smaller than 10")
        break