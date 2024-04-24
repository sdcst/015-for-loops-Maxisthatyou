#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
x = int(input("Enter an integer smaller than 10> "))
y = 0

if x >= 10:
    print(f"Invalid Input")
else:
    for i in range(1, x+1):
        y = y + int(i*str(1))
    else:
        print(f"the sum of the series is {y}")