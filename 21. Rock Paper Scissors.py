import random
rps=['rock', 'paper', 'scissors']
a=random.choice(rps)
b=random.choice(rps)
c=random.choice(rps)



print("This is a program for playing rock paper and scissors with computer.")
print("You have to write either rock, paper or scissors")
e=input("Enter: ")
print(a.capitalize())
f=input("Enter: ")
print(b.capitalize())
g=input("Enter: ")
print(f"{c.capitalize()}\n\n\n")


p1=0
p2=0


if (e.lower()=="rock" and a=="scissors") or (e.lower()=="paper" and a=="rock") or (e.lower()=="scissors" and a=="paper"):
    p1=p1+1
elif (e.lower()==a):
    p1=p1
else:
    p2=p2+1


if (f.lower()=="rock" and b=="scissors") or (f.lower()=="paper" and b=="rock") or (f.lower()=="scissors" and b=="paper"):
    p1=p1+1
elif (f.lower()==b):
    p1=p1
else:
    p2=p2+1


if (g.lower()=="rock" and c=="scissors") or (g.lower()=="paper" and c=="rock") or (g.lower()=="scissors" and c=="paper"):
    p1=p1+1
elif (g.lower()==c):
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