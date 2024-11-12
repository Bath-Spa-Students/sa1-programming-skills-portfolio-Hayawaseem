#Nested if statement
#To get the input from user
salary=(int(input("Enter your salary:")))
#if statement
if salary>=40000:
    year_of_experience=(float(input("Enter your year of experience:")))
    #if statement
    if year_of_experience>=3:
        print("You are eligible for this job")
    #else Statement
    else:
        print("Your experience is less than 3")
    #else Statement
else:
    print("You should earn 40k to eligible for this job")
