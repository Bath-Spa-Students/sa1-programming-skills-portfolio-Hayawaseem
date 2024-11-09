"""Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""

# Biography Advanced Requirements
# user iput
Name = input ("Enter full name: ")
Hometown = input ("Enter hometown: ")

# While loop functuion 
while True:                     # Loop start running until we tell it to stop
    Age = input ("Enter age: ")   
    if Age. isdigit():               # check if the input of age is only integer
        age = int(Age)
        break
    else:
        print ("Wrong age. Enter age in numbers ")

# Output
print (f"Name : {Name}")
print (f"Hometown : {Hometown}")
print (f"Age : {Age} ")