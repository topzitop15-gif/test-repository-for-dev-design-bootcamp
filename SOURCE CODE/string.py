# String : text in programming langauge "" are used for a string, once a quote is used wether on a number or alphabet it is referred to as a string

state = "kaduna"
alphabet = 'None'
empty = None
age_s = "45"

print((state))
print(type(state))

print("")
print("-----------------------")
print("")

print ("The length of the string 'kaduna' is:", len(state))

print("")
print("-----------------------")
print("")

# Transform to lower case
print("Nigeria" . lower())

print("")
print("-----------------------")
print("")

# Transform to upper case
print("america" . upper ())

print("")
print("-----------------------")
print("")

# Transform to title case
event_name = "uefa champions league"

print(event_name.title)

print("")
print("-----------------------")
print("")



#String slicing
sentence = "Chris Idakwo is in the class session which starts at 9am"
students = "David, Daniel, Sarah, Lola, Iniye, Irine"

# Index position by computing
# -1 less
greeting = "Hello, good morning"
print(greeting[1:5])

print(greeting[::-1])


#strip -removes characters on both sides
username = "_+  topzi.top15@gmail.com"
print("Username", username)
print("Username", username.strip("_+  "))


#rstrip removes trailing characters on the right hand side
print("Username", username.lstrip("_+  "))


#lstrip removes trailing characters on the (leading side)left hand side


# String Concatenation
first_name = "Temitope"
last_name = "Olugbamila"
score = 80

full_name = first_name + " " + last_name
print(full_name)

#Print out: John Doe scored 80 out of 100
print(first_name + " "+ last_name + " scored "  + str(score) +  " out of 100")



#String Formatting

sentence_f = f" {first_name} {last_name} scored {score} out of 100"
print (sentence_f)

sentence_fa = " {lname} {fname} scored {sc} out of 100 for this session" . format(
    fname=first_name, lname=last_name, sc=score)
print (sentence_fa)