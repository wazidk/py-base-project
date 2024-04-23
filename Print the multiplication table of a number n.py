# Print the multiplication table of a number n.
loop = 0
start = 1
distribute = 1 
while distribute >= loop :
        n = int(input("Input a Number ----->> "))
        range = int(input("Input Range  ----->> "))
        print(str(distribute) + " of " + str(loop))
        distribute +=  1 
        while start<=range :
            multiplication = n*start
            print(str(n) + " * " + str(start) + " = " + str(multiplication) )
            start += 1