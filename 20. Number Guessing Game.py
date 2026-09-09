import random
num1=random.randrange(0,50)
nu=int(input("Guess a number between 0-50: "))
while nu!=num1:
    # if num1 in (0,25) and nu in (25,50):
    if num1-nu>=25:
        print("Too Low!")
    elif num1-nu>=15:
        print("Low!")
    elif num1-nu>=5:
        print("Close but low!")
    elif num1-nu>=1:
        print("Too Close!")

    if nu-num1>=25:
        print("Too High!")
    elif nu-num1>=15:
        print("High!")
    elif nu-num1>=5:
        print("Close but High!")
    elif nu-num1>=1:
        print("Too Close!")

    nu=int(input("Try again: "))

print("You won!!")
print(f"The number is {num1}")