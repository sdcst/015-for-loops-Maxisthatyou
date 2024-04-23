#! python3
"""
The indexing variable starts with an initial value, and continues until the
indexing value reaches the ending value.

When 2 values are given, the initial value is set to be the first number
This will iterate through the sequence 10, 11, 12, 13, 14
"""

for i in range(10, 15):
    print(i)
else:
    print("We have printed the numbers 10 through 14!")
    
beginning = 10
ending = 15
for i in range(beginning, ending):
    print(i)
