# Student Grades Calculator
# Ask the teacher for the number of students
#For each student, ask for their name 
#For each student ask for test score
#Check if each score is valid(between 0 and 100)
#Calculate the average of all scores
# Tell the teacher :
#Who passed (score >= 60)
#Who failed (score < 50)
#the class average
#the highest and lowest score


print("\n" + "="* 50)
print("""
      STUDENT GRADES TRACKER PROJECT
      AUTHOR :TEMITOPE OLUGBAMILA
      DECSRIPTION: A PROGRAM THAT TRACKS STUDENT GRADES,CALCULATES CLASS AVERAGE, AND IDENTIFIES WHO PASSED
      """)
print("="* 50)
print("="* 50)


#step 1: Ask how many student
num_students = int(input("How many student do you want to grade? "))

#step 2: Initialize all necessary variables


total_score = 0
passed_students = []
failed_students = []

for num in range (num_students):
    print(f"\n ---Student {num +1} ---")

    # Ask student_name
    student_name = input ("Enter student name: ")

    #Get and validate student score
    student_score = float(input(f"Enter score for {student_name}:"))

    while student_score <0 or student_score >100:
        print("Invalid score! Please enter a score between 0 and 100.")
        student_score= float (input(f"Enter score for {student_name}: "))

    print ("Score recorded !") 

    #Add to the total for calcilation of average
    total_score = total_score + student_score  
    print ("The total score is:", total_score) 

    #Check if the student passed
    if student_score >= 60 :
        passed_students.append((student_name, student_score)) #tuple
    else: 
        failed_students.append((student_name, student_score))    

#tuples: items in a list that cannot be changed
#Calculate class average
class_average = total_score / num_students

print("class average ", class_average)

print("\n" + "="* 50)
print("STUDENT GRADES REPORT")
print("="* 50)


print("\n" + "="* 50)
print("\nSTUDENTS WHO PASSED")
for student in passed_students:
    print(f"")



