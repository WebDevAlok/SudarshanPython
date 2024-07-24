# Taking first term input "a" from the user
a = int(input("Enter the first term of the arithmetic sequence 'a' "))

# Taking common difference input "d" from the user
d = int(input("Enter the common difference of the arithmetic sequence 'd' "))

#Taking the limit "b" till which the sequence will be printed 
b = int(input("Enter the common difference of the arithmetic sequence 'b' "))
for i in range (a,b,d):
    print(i)