with open("files/Sample - Superstore.csv", "r") as file:
    #read and clean header
    header_line= file.readline().strip()
    columns= header_line.split(",")

    print("==========SUPERSTORE DATASET COLUMNS==========")
    for i, column in enumerate(columns, 1):
        print(f"{i:2}. {column}")