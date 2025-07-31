import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options1 = ["yes", "no"]

while True:
    user_input = input("Do you wanna play, boi? (yes/no) ").lower()


    if user_input not in options1:
        print("Invalid choice. Type 'yes', 'no', or 'q'.")
        continue

    if user_input == "no":
        print("Alright, maybe next time.")
        break

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid move. Try again.")
        continue

    computer_pick = random.choice(options)
    print("I picked", computer_pick + ".")

    if user_choice == computer_pick:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_pick == "scissors") or
        (user_choice == "paper" and computer_pick == "rock") or
        (user_choice == "scissors" and computer_pick == "paper")
    ):
        user_wins += 1
        print("Well done boi, you won!")

    else:
        computer_wins += 1
        print("Hahaha, I win boi!")

    print(f"Score: You {user_wins} - Computer {computer_wins}\n")
