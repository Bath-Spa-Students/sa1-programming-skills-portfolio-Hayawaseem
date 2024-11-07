"""Write a program that searches for a specific string whitin a list of strings. 
The list is initialized with specific name (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

# Names 
Names = ["Jack", "Zac", "Iran", "Ron", "Sam", "Dave"]
# Search name
Find_name = ("Sam")
# Input function 
Search_name = input ("Enter name you want to search: ")
# If function 
if Find_name in Names :
    print("found in the list" )
else:
    print("not found in the list" )

