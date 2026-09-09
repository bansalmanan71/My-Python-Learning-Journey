age=int(input("Enter your age here : "))
license=(input("Do you have a Driving License? (True or False) ")).strip().capitalize()
aadharcard=(input("Do you have aadhar card? (True or False) ")).strip().capitalize()
# Note - By using .strip(), True and False are not Case-Sensitive and .capitalize() converts inputs like "true", "TRUE", or "True" into "True".
print(license)
print(aadharcard)
#license = bool(license)
#aadharcard = bool(aadharcard)
if (age>=18 and license=="True" and aadharcard=="True"):
    print("You are eligible to Drive")
else:
    print("You are not eligible for driving")
    