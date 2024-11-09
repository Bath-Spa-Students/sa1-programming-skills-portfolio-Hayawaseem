"""Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly."""

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

 #Ask the user to input the month number
month = int(input("Enter month number from (1-12): "))

# Check if the month is in the dictionary
if month in month_days:
    if month == 2:  # Special case for February
        # Ask if it's a leap year
        leap_year = input("Is it a leap year? (yes or no): ")
    
        if leap_year == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        # Print the number of days for other months
        print(f"Month {month} has {month_days[month]} days.")
else:
    print("Wrong month number. Please enter a number between 1 and 12.")
