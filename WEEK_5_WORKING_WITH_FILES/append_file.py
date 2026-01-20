from datetime import datetime


file_path ="file/log.txt"

#add content to the end of the existing file
with open(file_path, "a") as file:
    file.write("n\n")
    file.write("")

    file.write("New entry: " + str(datetime))
