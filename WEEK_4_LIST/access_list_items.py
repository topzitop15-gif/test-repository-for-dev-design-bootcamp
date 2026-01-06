names = ["Tope", "Gen","Blessing","Mary","Peter","Wale","Keyu","Tobi","Sarah","Mide"]
print(len(names))
print("Returns the first item", names[0])
print("Returns the 6th item", names[5])
print("Last item", names[9])

#In the case youre not sure of times in a list, you can retrieve the last item using negative index
#Also using negative index lets yoy read a list from the back
print(" Returns the Last item using negative index:", names[-1])


#Alternative
index = len(names)-1
print(names[len(names)-1])

