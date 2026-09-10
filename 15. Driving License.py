age=int(input("Enter your age: "))
license=(input("Do you have a Driving License? (Yes or No): ")).strip().capitalize()
aadharcard=(input("Do you have aadhar card? (Yes or No): ")).strip().capitalize()
# Note - By using .strip() all the spaces from ahead and behind are striped and, True and False are not Case-Sensitive by using .capitalize(), itconverts inputs like "true", "TRUE", or "True" into "True".
#license = bool(license)
#aadharcard = bool(aadharcard)
if (age>=18 and license=="Yes" and aadharcard=="Yes"):
    print("You are eligible to Drive")
else:
    print("You are not eligible for driving")
    