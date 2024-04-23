# Print the multiplication table of a number n.
loop =30
distribute = 1 
while distribute == loop :
        n = int(input("Input a Number ----->> "))
        range = int(input("Input Range  ----->> "))
        print(str(distribute) + " of " + str(loop))
        start = 1
        distribute =+ 1 
        while start<=range :
            multiplication = n*start
            print(str(n) + " * " + str(start) + " = " + str(multiplication) )
            start += 1