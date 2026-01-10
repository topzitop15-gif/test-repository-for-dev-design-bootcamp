# get()method : used to retrieve a dictionary item by the key
from pprint import pprint
person = {
    "first_name" : "Tope",
    "last_name" : "Olu",
    "age" : 20,
    "pets" : {"dog": "Fredo", "cat" : "chunky"},
    "kids" : ["Joe","Martha", "Sarah"]

}

print("\n" + "="* 50)
print("GET METHOD")
print("="* 50)

print("First Name (with method):", person.get("first_name"))
print("First Name(without method):", person["first_name"])

print("\n" + "="* 50)

print("\n" + "="* 50)
print("CLEAR METHOD")
print("="* 50)

#clear method:clears out /deletes the dictionary content
person_b = {
    "first_name" : "Tope",
    "last_name" : "Olu",
    "age" : 20,
    "pets" : {"dog": "Fredo", "cat" : "chunky"},
    "kids" : ["Joe","Martha", "Sarah"]

}
person_b.clear()
pprint(person_b)


# copy function : it creates a shallow copy of the dictionary
print("\n" + "="* 50)
print("COPY FUNCTION")
print("="* 50)
person_a = person.copy()
pprint(person_a)


#Items: returns a list containing a tuple of each key-value pair
print("\n" + "="* 50)
print("ITEMS")
print("="* 50)
pprint(person.items())


#Values:returns a list of all the values in the dictionary
print("\n" + "="* 50)
print("VALUES")
print("="* 50)
pprint(person.values())


#Keys: returns a list of all the keys in teh dictionary
print("\n" + "="* 50)
print("VALUES")
print("="* 50)
pprint(person.keys())


#pop : removes the element with the specified key and returns the value
print("\n" + "="* 50)
print("POP")
print("="* 50)
last_name = person.pop("last_name")
print("The last name is :", last_name)
pprint(person)