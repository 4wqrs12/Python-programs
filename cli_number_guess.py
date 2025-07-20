import random

attempts = 0

secret_number = random.randint(0, 100)
print(secret_number)

while True:
    guess = int(input("Enter your guess for the secret number: "))

    if guess > secret_number:
        print("Your guess for the secret number is higher than the secret number! Guess lower!")
        attempts += 1
        continue
    elif guess < secret_number:
        print("Your guess for the secret number is lower than the secret number! Guess higher!")
        attempts += 1
        continue
    else:
        print(f"You found the secret number! You took {attempts} attempt(s)!")
        break
