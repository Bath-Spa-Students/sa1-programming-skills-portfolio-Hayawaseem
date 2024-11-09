"""Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question."""

#Primitive Quiz Advanced Requirements
# Dictionary of 10 European countries 
Capitals = {
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Monaco": "Monaco",
    "Norway": "Oslo"
}

# Quiz 
for country, capital in Capitals.items():
    answer = input(f"What is the capital of {country}? ")
    
    # Check answer ignoring case
    if answer.lower() == capital.lower():
        print("Right!")
    else:
        print(f"Wrong! The correct answer is {capital}.")