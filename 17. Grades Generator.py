print("This is a program to grade the student depending on their marks")
marks=int(input("Enter your marks (Out of 100) : "))

if marks < 100:
    if marks>=95:
        print("Grade : S")
    elif marks>=90:
        print("Grade : A+")
    elif marks>=85:
        print("Grade : A")
    elif marks>=80:
        print("Grade : B+")
    elif marks>=75:
        print("Grade : B")
    elif marks>=70:
        print("Grade : C+")
    elif marks>=65:
        print("Grade : C")
    elif marks>=60:
        print("Grade : D+")
    elif marks>=55:
        print("Grade : D")
    else:
        print("Your marks are lower than 55")
else:
    print("Marks cannot be greater than 100, Please try again.")