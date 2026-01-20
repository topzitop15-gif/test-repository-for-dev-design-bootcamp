from pprint import pprint

person= {
    "first_name" : "Tope",
    "last_name" : "Olu",
    "age" : 20,
    "pets" : {"dog": "Fredo", "cat" : "chunky"},
    "kids" : ["Joe","Martha", "Sarah"]

}

person["middle_name"] = "Dummy"

pprint(person)