# count the number of students with the “A” grade in the following tuple.
print("Count the number of students with any grade .")
grade = ("C","A","A+","A","D","A")
count_grade = input("Input Grade --->> ")


if grade.count(count_grade) == 0 :
    print("Not Found")
else:
    print("The number of students with the " + count_grade + " grade is "+ str(grade.count(count_grade)))