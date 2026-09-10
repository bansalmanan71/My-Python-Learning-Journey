import random
rps=['rock', 'paper', 'scissors']
a=random.choice(rps)
b=random.choice(rps)
c=random.choice(rps)



print("This is a program for playing rock paper and scissors with computer.")
print("You have to write either rock, paper or scissors")
e=input("Enter: ")
print(a)
f=input("Enter: ")
print(b)
g=input("Enter: ")
print(f"{c}\n\n\n")


p1=0
p2=0


if (e=="rock" and a=="scissors") or (e=="paper" and a=="rock") or (e=="scissors" and a=="paper"):
    p1=p1+1
elif (e==a):
    p1=p1
else:
    p2=p2+1


if (f=="rock" and b=="scissors") or (f=="paper" and b=="rock") or (f=="scissors" and b=="paper"):
    p1=p1+1
elif (f==b):
    p1=p1
else:
    p2=p2+1


if (g=="rock" and c=="scissors") or (g=="paper" and c=="rock") or (g=="scissors" and c=="paper"):
    p1=p1+1
elif (g==c):
    p1=p1
else:
    p2=p2+1



if p1>p2:
    print("Congratulations You WON!!!")
elif p1==p2:
    print("The Match was a Draw.")
elif p2>p1:
    print("You lost.")
print(f"You have {p1} points and computer has {p2} points.")