"""Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.
Instructions:

1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.
  
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month."""

# Days of the month
month_days = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31,  # December
}
# user input
month = int(input("Enter month number (1-12): "))
# if-else statement
if 1 <= month <= 12:
    print (f"Number of days : {month_days[month]}")
else:
    print (f"Invalid month number")
