"""Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the

password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted."""

# Brute Force Attack
# correct password 
right_password = "1234"
# Maximum attempts
max_attempts = 5
# Accepted attempts 
attempts_accept = 0

# While loop function
while attempts_accept < max_attempts:
    password = input("Enter password: ")  # user input 

    if password == right_password:  # Check if password matches 
        print("Access granted")
        break
    else:
        attempts_accept += 1  # Increase the number of attempts
        remaining_attempts = max_attempts - attempts_accept  # Calculate remaining attempts
        if remaining_attempts > 0:
            print(f"Wrong password! You have {remaining_attempts} attempts left")  # Inform user of remaining attempts
        else:
            print("maximum attempts allowed")