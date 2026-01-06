# Logical operators: are used to combine or modify comparison operations
# they help python answer bigger questions made up os smaller true/false questions

age = input("Enter your age: ")
has_id = input("Do you have an ID? (Yes/No): ")

#TO DO:Use input to take data. Validate response for has_id to Yes or No

#And operator : all sides of the sttsement must be true else it resolves false
if age >= 18 and has_id == True:
    print("Give access")

else:
    print("No access")




#Or operator : only one side of the statement can be true

if age >= 18 or has_id == True:
    print("Give access")

else:
    print("No access")      


#Not operator : gives you a reverse of a condition
#print(not (5 == 5))
logged_in = True
if not logged_in:
    print("You're a guest")
else:
    print("Welcome back")

