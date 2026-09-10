age=int(input("Enter your age: "))
has_license=(input("Do you have a Driving License? (Yes or No): ")).strip().lower() in ["yes", "y", "ye", "true", "yea", "yeah", "ya"]
has_aadharcard=(input("Do you have aadhar card? (Yes or No): ")).strip().lower() in ["yes", "y", "ye", "true", "yea", "yeah", "ya"]
# Note - By using .strip() all the spaces from ahead and behind are striped
#aadharcard = bool(aadharcard)
if (age>=18 and has_license and has_aadharcard):
    print("You can drive.")
else:
    print("You can NOT drive.")
    