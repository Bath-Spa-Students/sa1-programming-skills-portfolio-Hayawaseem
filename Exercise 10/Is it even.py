"""Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function."""

# Is it even ?

def even_odd(number):
# check if the number is dividable by 2
    if number % 2 == 0:
        return (f"The number is even.")
    else:
        return (f"The number is odd.")
    
# main function to control the code
def main():
# ask user to input 
    entered_value = int(input("Enter number: "))
    result = even_odd(entered_value)
    print(result)
    
# check if the text is run directly
if __name__ == "__main__": 
    main()