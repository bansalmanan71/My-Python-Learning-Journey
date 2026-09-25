print("This program calculates the factorial of any given integer.")
a=int(input("Which integer's factorial do you want?: "))
factorial=1
while a>0:
    factorial=factorial*a
    a=a-1

print(factorial)