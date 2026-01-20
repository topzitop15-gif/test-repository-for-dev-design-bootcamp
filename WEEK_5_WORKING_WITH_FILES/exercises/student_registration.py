file_path = "../files/registration.txt"
full_name = input("Enter your full name: ")
class_level = input("Enter your class level(SS1,SS2,SS3):")
age= input("Enter your age: ")

with open(file_path, "a") as file:
    file.write(f"{full_name} | {class_level} | {age}" + "\n")