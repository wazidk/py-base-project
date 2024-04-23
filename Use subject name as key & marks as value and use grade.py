# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
# Use subject name as key & marks as value and use grade
Student_Name = input("Student Name : ")

x = int(input("Enter Physics : "))
y = int(input("Enter Chemistry "))
z = int(input("Enter Maths : "))

marks = {
    "Physics " : x ,
    "Chemistry " : y ,
    "Maths " : z
}


if(x >= 90):
    markx ="A+"
elif(x >= 80):
    markx ="A"
elif(x >= 70):
    markx ="A-"
elif(x >= 60):
    markx ="B"
elif(x >= 50):
    markx ="C"
elif(x >= 33):
    markx ="D"
elif(x <33):
    markx ="F"
else: print("You Enter Wrong Mark")


if( y>= 90):
    marky ="A+"
elif(y >= 80):
    marky ="A"
elif( y>= 70):
    marky ="A-"
elif(y >= 60):
    marky ="B"
elif(y >= 50):
    marky ="C"
elif(y >= 33):
    marky ="D"
elif(y<33):
    marky ="F"
else: print("You Enter Wrong Mark")

if( z>= 90):
    markz ="A+"
elif(z >= 80):
    markz ="A"
elif( z>= 70):
    markz ="A-"
elif(z >= 60):
    markz ="B"
elif(z >= 50):
    markz ="C"
elif(z >= 33):
    markz ="D"
elif(z<33):
    markz ="F"
else: print("You Enter Wrong Mark")


student = {
    "Student_Name " : Student_Name,
    "Physics " : markx ,
    "Chemistry " : marky ,
    "Maths " : markz 
}

print(student["Student_Name "])

print(  "Physics --> " + str(student["Physics "]))

print(  "Chemistry --> " + str(student["Chemistry "]))

print(  "Maths --> " + str(student["Maths "]))
