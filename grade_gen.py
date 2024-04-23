Student_Name = input("Student Name : ")
Subject_name = input("Subject Name : ")

Subject_marks = int(input("Subject marks : "))


if(Subject_marks >= 90):
    mark ="A+"
elif(Subject_marks >= 80):
    mark ="A"
elif(Subject_marks >= 70):
    mark ="A-"
elif(Subject_marks >= 60):
    mark ="B"
elif(Subject_marks >= 50):
    mark ="C"
elif(Subject_marks >= 33):
    mark ="D"
elif(Subject_marks <33):
    mark ="F"
else: 
    print("You Enter Wrong Mark")


print(Student_Name + " pass  the mark of " + str(Subject_marks) + " of the grade " + mark + " in the subject " + Subject_name + ".")
