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