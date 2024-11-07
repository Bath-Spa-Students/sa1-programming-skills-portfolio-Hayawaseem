"""In this exercise, youll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the uses answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong."""

# User input 
Capital = input("What is the capital of France?")
  # provides feedback
if Capital. strip().lower() == "paris" :
    print ("answer is correct!")
else: 
    print ("answer is wrong!") 
