file_path = "files/greeting.txt"

#write content to one line at a time
with open(file_path, "w") as file:
    file.write("Hello, this is anew line entry in a new file!\n")
    file.write("This is another new line!")



#write multiple lines at once
    names = ["Gospel Ibe", "Tola Kem","Moyin Simbiat","Deborah Ene","Kemi Oge"]


    newnames = []
    for name in names:
        newnames.append(f"{name}\n")

    print(newnames)
    file.writelines(newnames)

    #option 2: introduce a new line character with each name in list using a list comprehension
    newnames= [f"{names}\n" for name in names]

    print(newnames)
  



   

