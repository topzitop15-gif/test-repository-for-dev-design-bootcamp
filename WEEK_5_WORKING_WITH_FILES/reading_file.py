#Relative path
file_path ="files/example.net"

with open(file_path, "r") as file:
    for line in file:
        print (line)

    print("")
    print("")
    print("")
    


    #reset the file pointer back to the first line
    file.seek(0)

    content= file.read()
    for line in content.split("\n"):
        print(line)
        