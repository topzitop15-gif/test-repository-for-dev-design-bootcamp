from pprint import pprint


car = dict(
    brand ="ford",
    model = "Mustang",
    enginelitre = 5.0,
    transmission ="manual" 
)
print("\n" + "="* 50)
#You access values in a dictionary using a square breacket and the name of the key as a string wuithin the bracket
brand= car["brand"]
print("car brand is:", brand)


print("\n" + "="* 50)



person = {
    "first_name" : "Tope",
    "last_name" : "Olu",
    "age" : 20,
    "pets" : {"dog": "Fredo", "cat" : "chunky"},
    "kids" : ["Joe","Martha", "Sarah"]

}

print("What is the name of the 2nd child?")
second_child = person["kids"][1]
print("Name of the 2nd child is:", second_child)

print("\n" + "="* 50)

print("What is the name of his dog?")
dog_name = person["pets"]["dogs"]
print("What is the name of the dog is:",dog_name)

