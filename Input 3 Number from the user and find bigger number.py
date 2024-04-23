#Input 3 Number from the user and find bigger number
a = int(input("Your 1st Number -->"))
b = int(input("Your 2nd Number -->"))
c = int(input("Your 3rd Number -->"))

if(a>=b and a>=c):
    print(str(a) + " is the bigger number of those 3 number.")
elif(b>=c ):
    print(str(b) + " is the bigger number of those 3 number.")
else: 
    print(str(c) + " is the bigger number of those 3 number.")

