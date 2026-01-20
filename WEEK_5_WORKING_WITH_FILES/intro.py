#method used in accessing files

#Step1:Opening and reading of files
file = open("files/Sample - Superstore.csv", "r")
content = file.read()
file.close()

#print(content)

#Absolute file path- shows the full path definition/name,from the root down to the end of the file itself


#Relative file path:are relative to the file referencing them, part to the file relative to the python file importing it

#file path-path to the file on your laptap/desktop or cloud/online

#Step 2: Reading line ny line (Row by Row)
file_= open("files/Sample - Superstore.csv", "r")

#Read first line(usually the header line)
header = file_.readline().strip()
header= header.split(",")

#Read all other lines
for line in file_:
    print(line.split(","))
    print("=" * 20)

file_.close()


#Step3: Using 'with' statement (best practice)
with open("files/Sample - Superstore.csv", "r") as file:
    #read header
    header = file.readline().strip()
    print("Columns:", header)

    for line in file:
        print(line.split())
        print("=" * 20)
    

