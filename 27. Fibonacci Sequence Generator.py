print("This is a program to generate Fibonacci Series till a user-specified limit which is taken as input from the user.")
a=int(input("Enter the limit: "))

def fibonacci(a):
    f0=0
    f1=1
    print(0,1,sep=",", end=",")
    for i in range(a-2):
        f2=f0+f1
        f0=f1
        f1=f2
        print(f2, end=",")

fibonacci(a)
    

# Fibonacci Series: 0,1,1,2,3,5,8,13,..............
# Sum of last two digits