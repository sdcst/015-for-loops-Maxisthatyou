"""
We don't need to use the indexing variable, sometimes it is just a counter to keep track of how many times we need to repeat something.

This program will ask the user to enter in 3 numbers, and then find the sum of them.
It uses a variable to keep track of the running total as each number is entered.
"""

total = 0
print("You will enter in 3 numbers and this program will find the sum.")
print()
for i in range(3):
    num = i + 1
    strNum = input(f"Enter in number {num}>")
    intNum = int(strNum)
    total = total + intNum
print(f"The total of your numbers is {total}")

"""
Things to think about:
Why did we add 1 to i in line 12?
What is happening in line 15?
"""

