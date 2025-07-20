import random
import time

print("""
Math Game
""")

score = 0


while True:
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    math_opt = input('Enter which operation you want to be tested on (+, -, *, / or "~" to finish): ')
    if math_opt != "+" and math_opt != "-" and math_opt != "*" and math_opt != "/" and math_opt != "~":
        print("That is not a valid option. Please input +, -, *, /")
    else:
        if math_opt == "+":
            answer = num1 + num2
            while True:
                try:
                    guess = int(input(f"What is {num1} + {num2} ?: "))
                    break
                except ValueError:
                    print("That is not valid character! Please enter a whole number!")
                    time.sleep(2)
                    continue
            if guess == answer:
                print("Correct!")
                score += 1
                print("You scored a point!")
            else:
                print("Incorrect!")
                score -= 1
                print("You lost a point!")
        elif math_opt == "-":
            answer = num1 - num2
            while True:
                try:
                    guess = int(input(f"What is {num1} - {num2} ?: "))
                    break
                except ValueError:
                    print("That is not valid character! Please enter a whole number!")
                    time.sleep(2)
                    continue
            if guess == answer:
                print("Correct!")
                score += 1
                print("You scored a point!")
            else:
                print("Incorrect!")
                score -= 1
                print("You lost a point!")
        elif math_opt == "*":
            answer = num1 * num2
            while True:
                try:
                    guess = int(input(f"What is {num1} * {num2} ?: "))
                    break
                except ValueError:
                    print("That is not valid character! Please enter a whole number!")
                    time.sleep(2)
                    continue
            if guess == answer:
                print("Correct!")
                score += 1
                print("You scored a point!")
            else:
                print("Incorrect!")
                score -= 1
                print("You lost a point!")
        elif math_opt == "/":
            answer = round(num1 / num2, 3)
            while True:
                try:
                    guess = float(input(f"What is {num1} / {num2} (round to hundredths place if needed to) ?: "))
                    break
                except ValueError:
                    print("That is not valid character! Please enter a whole number!")
                    time.sleep(2)
                    continue
            if guess == answer:
                print("Correct!")
                score += 1
                print("You scored a point!")
            else:
                print("Incorrect!")
                score -= 1
                print("You lost a point!")
        elif math_opt == "~":
            print(f"You scored {score} point(s)!")
            time.sleep(2)
            break
