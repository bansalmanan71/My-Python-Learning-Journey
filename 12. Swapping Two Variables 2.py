# In this program, we will swap values of two variables without taking a third, temporary variable


print("In this program we will swap values of two variables a & b")
num1=float(input("Enter the value of num1 : "))
num2=float(input("Enter the value of num2 : "))

num1=num1+num2
num2=num1-num2
num1=num1-num2


#Algorithm
# a'=a+b
# b'=a'-b    ----> b'=a
# a"=a'-b'   ----> a"=(a+b)-a  -----> a"=b

print("The value of num1 is : ", num1)
print("The value of num2 is : ", num2)







# The above code was for swapping two numbers without taking a temporary, third variable
# By taking third variable, code is easy and simple however the above algorithm is good.