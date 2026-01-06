found = False
for num in range(1, 1001):
    guess = int(input("Guess the number:"))
    if guess== 42:
        found = True
        print ("Correct!")

    if not found:
        print ("Try again")    

#with loop control
for num in range(1, 1001):
    guess = int(input("Guess the number:"))
    if guess== 42:
        print ("Correct! You have found the number")        
        break #ends/exists the parent loop completely

    print("Try again!")


#Even numbers (up to 20)
for num in range (1, 1001):
    if num > 20:
        print ("What is the value of num?, num")
        break


#TO DO:
    





    
    