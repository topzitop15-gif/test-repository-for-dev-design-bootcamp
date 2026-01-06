#light = "yellow"
#TO DO : modify  colors into list

    #one equal to(=) is used as an assignment
    #double equal to(==) is used for comparison
 #allowed colors(red,yellow, green)


    # If  else statement
    #If clause
    # If condition : code that runs of the condition is true
 # Else clause:code that runs if the condition is false 
    # the else statement is like a catch all phrase


#TO DO; take input and validate to ensure its among allowed/permitted colors
#TO DO: Use while loop
light = input("What color is the traffic light?"). lower()

print("What is light", light)

if light == "red" or light == "yellow" or light == "green":
    
    if light == "green" or light == "blinking":
        print("Go")                
    elif light == "yellow":     
        print("slow down")
    elif light =="red":
        print("stop")
    else:
        print("stop")
else:
    print("Valid colors are red, yellow, green only")
        



       



temperature = 15
humidity = 15

# read more on truth table
if temperature > 30 or humidity < 20:
    print("Warning:unusual weather condition detected")
else :
    print("Weather conditions are normal")      
