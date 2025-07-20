import random
import time

print("Really bad Password Generator \n")
time.sleep(2)

letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = "!@#$%^&*()"
numbers = "1234567890"

letters_list = list(letters)
upper_letters_list = list(upper_letters)
characters_list = list(characters)
numbers_list = list(numbers)

while True:
    print("Your password is: ")
    for generate_password in range(2):
        print(random.choice(letters_list) + random.choice(upper_letters_list) + random.choice(characters_list) + random.choice(numbers_list), end="")

    print(" \n")
    question = input("Do you want to generate a new password? (y/n): ")
    if question == "y":
        continue
    else:
        break
