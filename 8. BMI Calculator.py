print("This is a program to Calculate your BMI (Body Mass Index)")
print("BMI Between 18 to 21 is considered Normal")
height=float(input("Enter your Height (In CM) : "))
weight=float(input("Enter your Weight (In KGs) : "))
height_in_meter=height/100
BMI=weight/(height_in_meter*height_in_meter)
print("Your BMI is : ", BMI)