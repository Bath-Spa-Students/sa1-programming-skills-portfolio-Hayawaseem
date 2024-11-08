"""Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project."""

# Some Counting

# Loop that counts up from 0 to 50 in increments of 1
print("\nCounting up from 0 to 50:")
for number in range(0, 51, 1):
    print(number)

# Loop that counts down from 50 to 0 in decrements of 1
print("\nCounting down from 50 to 0:")
for value in range(50, -1, -1):
    print(value)

# Loop that counts up from 30 to 50 in increments of 1
print("\nCounting up from 30 to 50:")
for num in range(30, 51, 1):  
    print(num)

# Loop that counts down from 50 to 10 in decrements of 2
print("\nCounting down from 50 to 10 in decrements of 2:")
for numeral in range(50, 9, -2):
    print(numeral)

# Loop that counts up from 100 to 200 in increments of 5
print("\nCounting up from 100 to 200 in increments of 5:")
for digit in range(100, 201, 5):
    print(digit)