""" 
find the sum of the numbers 1 to 50
print finished when done
"""
total = 0
for i in range(51):
    total = i + total
else:
    print("finished!")
    print(f"The sum of all the numbers from 1 to 50 is {total}")
