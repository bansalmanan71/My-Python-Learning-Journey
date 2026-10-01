print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("Welcome to Kaun Banega Crorepati!!!")
print()
print("In this program, you will be given a real set of questions that you have to answer, and if you answer them right, you win cash rewards.")
print()
print("You will get 3 hearts, if you get any answer wrong, then you lose 1 heart and game will finish if you finish all of your hearts")
print()
print("For every correct answer, you get money 500 * Question_number")
print()
print("For every wrong answer, you lose 150 * Question_number")
print()
print("Total prize you can win from here is ₹27,500")

# ques=["Q1. What is the capital of Nigeria?","Q2. What is the approximate GDP of United States of America?"]
ques = [
    "Question 1 (Level: Easy - General Knowledge)\nWhich of these words is most commonly used to greet someone when picking up a telephone call?",
    "Question 2 (Level: Easy - Bollywood)\nIn the iconic 1975 Hindi movie Sholay, what was the name of the character played by Amitabh Bachchan?",
    "Question 3 (Level: Easy - Sports)\nWho is the only Indian cricketer to have scored 100 international centuries?",
    "Question 4 (Level: Medium - Hindu Mythology)\nAccording to the Mahabharata, who among the following was not raised as one of the five Pandava brothers?",
    "Question 5 (Level: Medium - Indian Geography)\nWhich of these Indian states does NOT share an international land border with Nepal?",
    "Question 6 (Level: Medium - Indian Politics & History)\nWho holds the distinction of being the first woman to become the Chief Minister of an Indian state?",
    "Question 7 (Level: Hard - Science & Technology)\nWhat is the name of the rover that successfully rolled out onto the lunar surface as part of India's historic Chandrayaan-3 mission?",
    "Question 8 (Level: Hard - Global Affairs)\nThe headquarters of which of these global organizations is located in Geneva, Switzerland?",
    "Question 9 (Level: Very Hard - Literature)\nWho was the first Indian citizen to win the prestigious Booker Prize for a novel?",
    "Question 10 (Level: Jackpot / Crorepati - History)\nWhich Mughal Emperor was born with the name Muhi-ud-Din Muhammad?"
]

option = [
    "A) Bye\nB) Hello\nC) Please\nD) Sorry",
    "A) Veeru\nB) Thakur\nC) Jai\nD) Gabbar",
    "A) Virat Kohli\nB) Rohit Sharma\nC) Sunil Gavaskar\nD) Sachin Tendulkar",
    "A) Nakula\nB) Sahadeva\nC) Karna\nD) Arjuna",
    "A) Uttarakhand\nB) Uttar Pradesh\nC) Himachal Pradesh\nD) Bihar",
    "A) Sarojini Naidu\nB) Sucheta Kripalani\nC) Indira Gandhi\nD) J. Jayalalithaa",
    "A) Vikram\nB) Pragyan\nC) Aditya\nD) Vyommitra",
    "A) World Health Organization (WHO)\nB) United Nations (UN) Headquarters\nC) International Monetary Fund (IMF)\nD) World Bank",
    "A) Salman Rushdie\nB) Aravind Adiga\nC) Arundhati Roy\nD) Kiran Desai",
    "A) Shah Jahan\nB) Aurangzeb\nC) Jahangir\nD) Bahadur Shah Zafar"
]

ans = [
    "b", 
    "c", 
    "d", 
    "c", 
    "c", 
    "b", 
    "b", 
    "a", 
    "c", 
    "b"
]
hearts=3
money=0
for o in range(len(ques)):
    print("\n\n\n\n\n")
    print(f"Your Current Balance is ₹{money}\nand you have {hearts} hearts right now.\n")
    print(f"Here is Question {o+1}. ")
    print()
    print(ques[o])
    print(option[o])
    ans1=input("Enter the right option (a,b,c,d): ")
    if ans1.lower().strip()==ans[o]:
        money=money+(500*(o+1))
    else:
        money=money-(150*(o+1))
        hearts-=1
    if hearts==0:
        # print("\n\nYou have 0 hearts remaining.")
        break

# print("\n\n\n\n\nYou have successfully completed the Kaun Banega Crorepati!")
# if money>0:
#     print(f"Congratulations for winning ₹{money} cash!!!")

print("\n\n\n\n\n=======================================")
if hearts==0:
    print("GAME OVER! You lost all your hearts.")
    print(f"You are walking away with ₹{money}.")
else:
    print("You have successfully completed Kaun Banega Crorepati!")
    if money > 0:
        print(f"Congratulations for winning ₹{money} cash!!!")
    else:
        print(f"You finished the game, but your balance is ₹{money}. Better luck next time!")

print("\n\n\n\n\n")









# Some things to tinker upon:
# 1. Can we add a timer on each question using import time
# 2. Can we update the questions dynamically
# 3. Can we add a 50-50 option which eliminates two options and tells user that the answer is between these two, if we do it so, we will give user 3 times this magic button, user could type 50-50 in chat and two options will get eliminated, we can do this by creating a 50-50 list and using if else block at logic loop.
# 4. Can we convert this into a GUI later