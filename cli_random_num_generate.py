import random
import time

print("""
Random Number Generator
""")

while True:

    count = 0

    while True:
        try:
            min = int(input("Enter the minimum value: "))
            max = int(input("Enter the maximum value: "))
            break
        except ValueError:
            print("Please enter a non-negative integer! (Ex: 2, 5, 1, 0, 100)")
            continue

    generate_number = random.randint(min, max)

    print(f"The random number generated that is between {min} and {max} is: {generate_number}")

    question = input("Do you want to generate another random number? (y/n): ")
    if question.lower() == "y":
        continue
    else:
        for animation in range(4):
            print("Exiting"+"."*count)
            count += 1
            time.sleep(0.69)
        time.sleep(random.randint(1, 3))
        break
