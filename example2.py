"""
This loop will repeat the print statement 10 times.
Note that when we use the for loop, i, the loop variable.  It will
store the value of whatever you using to count and it changes every
time you perform an "iteration" through the loop.

The iteration starts at an initial value of 0 (not 1) and ends at the
integer value BEFORE your end value.  In this case, it goes from 0 - 9
and takes on all the integer values inbetween.

Note:  The ending value must be an integer.

The indexing variable can be used in calculations within the loop!

"""

for i in range(10):
  double = 2 * i
  print(f"The number right now is {i} and its doubled value is {double}")
else:
  print("We are finished!")
