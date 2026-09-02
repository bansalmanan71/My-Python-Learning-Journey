print("This is a program to print the greatest of the three numbers")
a=int(input("Enter Your 1st Number : "))
b=int(input("Enter Your 2st Number : "))
c=int(input("Enter Your 3st Number : "))

if a>b and a>c:
    print("a is the greatest number.")
elif b>c:
    print("b is the greatest number.")
else:
    print("c is the greatest number.")