# A dictionary is data type or structure used to store data values in key-value pairs
# A dictionary is an ordered collection (as from python 3.17) which is changeable/muteable 
# The values in a dictionary can be of any data type
# The keys must be strings, they cannot be duplicate
# {}
# The keys must have a unique name
#You can have any amount of dictionaries under a list

#first_name
#last_name
#dob
#gender
#email
#phone
#current_stat
#class_group
#height
#weight
#nok_name
#nok_phone
#nok_email

from pprint import pprint
student_profile= {
    "first_name" : "Temitope",
    "last_name" : "Olu",
    "age" : 26,
    "height" : 5.10,
    "gender" : "female",
    "registered" : "true",
    "skills" : []

} 
#prettyprint: to print something to make it look fine (pprint)
#pprint (student_profile)

#for num in range(1000):
#    fname=input("Enter your first name: ")


"""orders =[ {
    "orderid": "23456",
    "orderdate" : 4554,

}]"""

#Create dictionary using dict() constructor
student_b = dict(
    first_name = "Tope",
    last_name = "Olu",
    age = 26,
    height = 5.10,
    weigth = 120,
    gender = "female"
)
pprint (student_profile)
print("\n" + "="* 50)
pprint(student_b)