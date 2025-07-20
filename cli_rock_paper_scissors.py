import random
import time

score = 0

while True:
    user_choice = input("Enter rock, or paper, or scissors (options: rock, paper, or scissors): ")
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Please enter a valid option! (r, p, s)")
    else:
        computer = random.randint(1, 3) # computer_choice = 1 --> Rock, computer_choice = 2 --> Paper, # computer_choice = 3 --> Scissors
        if computer == 1:
            computer_choice = "rock"
        elif computer == 2:
            computer_choice = "paper"
        elif computer == 3:
            computer_choice = "scissors"
        print(f"Player chose: {user_choice} and computer chose: {computer_choice}")
        time.sleep(2)

        if user_choice == computer_choice:
            print(f"Tie! Both sides picked {user_choice}!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("User wins!")
                score += 1
            else:
                print("Computer wins!")
                score -= 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("User wins!")
                score += 1
            else:
                print("Computer wins!")
                score -= 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("User wins!")
                score += 1
            else:
                print("Computer wins")
                score -= 1
    question = input("Do you want to continue (y/or any key to quit) ?: ")
    if question.lower() == "y":
        continue
    else:
        print(f"Your final score is: {score}")
        break
