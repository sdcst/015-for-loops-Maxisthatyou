## SDSS Computing Studies Python Assignment
### Assignment #012 For Loops (Total Marks 15)

Objectives:
* Use a for loop to repeat some code a number of times

For loops are useful when you want to repeat a section of code a set number of times. They are extremely important structures in programming, as they can be used to cycle through large amounts of data, processing each. An example might be if you had a cookbook and you were flipping through the pages.  You can cycle through all of the pages looking for a specific page that you are interested in.

Although there are numerous ways that we can use a for loop, but today we will be focusing on repeating a set number of times using a number or integer value.

### Using a range
We will use a for loop to repeat a task a certain number of times.
Look at example1.py


### Note: A for loop can't be empty
If for some reason you need to execute no commands inside a for loop,
you need to use the command "pass"

example:
```
for i in range(3,5):
    pass
print("All done!")
```
### XX Tasks

##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop.
(2 points) 

###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65

(2 points)

##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
(2 points)

##### Task 4
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You may need 2 nested loops to draw the contents of
1 row and the number of rows.

##### Problem 2
Calculate the factorial of a number. 
A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

