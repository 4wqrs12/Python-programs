import random
import time

print("""
Penny Flipper
""")

time.sleep(2)

def flip_penny():
    answer = random.randint(1, 2)

    if answer == 1:
        print("Heads!\n")
    else:
        print("Tails!\n")

while True:
    count = 0 
    for wait_time in range(3):
        print("Flipping."+"."*count)
        time.sleep(1)
        count += 1

    flip_penny()
    
    question = input("Do you want to flip again? (y/n): ")
    print()
    if question.lower() == "y":
        continue
    else:
        break
