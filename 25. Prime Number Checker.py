print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("This is a program to determine whether the number taken as input from the user is a prime number or not.")

num1=int(input("Enter the number: "))
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
for i in range(2,num1):
    if num1%i==0:
        print(f"The number {num1} is not a prime number because it is divisible by {i}.")
        break
else:
    print(f"The number {num1} is a prime number.")