# Void Function returns nothings . It executes the statement and prints 
# Value returning function returns takes input perform operations and return 
# function name must be descriptive like square function , random function 
# We use def keyword to create any function  # Function header 
# Be careful regarding indentation 
# Void function
def print_message():
    print("Hello Students")

# Calling function
print_message()

# Local variable
def print_message():
    message = "Hello Students"  # Local variable
    print(message)

# Calling function
print_message()

# Attempt to print a local variable outside its scope will result in an error:
# Uncommenting the following line would raise an error since `message` is not defined in the global scope.
# print(message)

# Different functions having the same local variable names - No syntax error
def print_message():
    message = "hy"
    print(message)

def print_message_2():
    message = "hello"
    print(message)

print_message()
print_message_2()

# Passing argument to a function
def print_message_2(message):  # parameter
    print(message)

msg = "Good Morning"
print_message_2(msg)  # Argument

# Example: A parameter `x` stores a value and doubles it
def main():
    value = 5
    show_double(value)

def show_double(x):
    print(x * 2)

# Calling the main function
main()