#! python3
"""
The indexing variable starts with an initial value, and continues until the
indexing value reaches the ending value.

If only 1 value is included, it is assumed to be the ending value and the
beginning value is 0

If two values are given, the first is the beginning value:
example 3.py
"""

# in this loop example, no starting value is given
# the loop will start at 0, and continue. It will not include 10, but will stop at 9
for i in range(10):
    print(i)
