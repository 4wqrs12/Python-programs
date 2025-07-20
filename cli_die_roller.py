import random
import time



while True:
    count = 0

    number_rolled = random.randint(1, 6)

    question = input("Do you want to roll the die?(y/n): ")

    if question.lower() == "y":
        for rolling in range(4):
            print("Rolling"+"."*count)
            count += 1
            time.sleep(0.69)
        time.sleep(1)
        print(f"You rolled a: {number_rolled} ! ")
    else:
        break
