import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type rock/paper/scissors or "Q" to quit.") . lower()
    if user_input == "q":
        break
    if user_input not in ["rock","paper","scissor"]:
        print("Not a valid string")
        continue
    
    random_number = random.randint(0,2)
    