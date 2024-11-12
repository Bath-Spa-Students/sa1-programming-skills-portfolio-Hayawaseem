# Homogeneouse List
List = ["Haya", "Business", "hayasflowers"]
print (List)

# Hetrogeneous List
Order = ["Fastfood", "18", "7.5"]
print (Order)

# Homogeneous order
Subject = ["English", "Maths", "Arts"]
print (Subject)

# Hetrogeneous order
Work = ["59", "20.8", "Code"]
print (Work)

# Repetition satement
Names = ["Haya", "Tayyaba", "Ayesha", "Fathima"]
# Value name
Name_Value = Names * 3 
# print statement
print (Name_Value)

# positive indexing start from left to right 
# for example; number = [1,2,2,3,5,]
                       #[0,1,2,3,4] 
                       #print =(number[1])
# negativce indexing start from right to left 
# for example : number = [3,4,6,7,8]
                      # [-5,-4,-3,-2,-1]

# lens function tells us number of items in the list 
numbers = [1,2,3,4,5,6]
print ("number of elements in the list :" ,len (numbers))
# Mutability (changeable) value 
numbers = [1,2,3,4,5,6]
        # [0,1,2,3,4,5]
numbers [0]=1
print (numbers)
# concatenation 
List_1 = [1,2,3,4,5,6]
List_2 = [7,8,9,10,11]
list_3 = List_1 + List_2
print (list_3)

# built in method.index
List_4 = [1,2,3,4,5,6,7,88,89,90,890,600]
print (List_4.index (600))