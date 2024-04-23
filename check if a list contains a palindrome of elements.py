# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list = [1, 2, 3, 2, 1]

copy_list = list.copy()
copy_list.reverse()

if list == copy_list: 
    print("Palindrome")
else:
    print("Non Palindrome")