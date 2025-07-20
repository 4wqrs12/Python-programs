import time
import math
import random


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def expo(num1, num2):
    return pow(num1, num2)


def sq_ro(num1):
    return math.sqrt(num1)


print("""
Calculator
""")

while True:

    count = 0

    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponent
    6. Calculate Square Root
    7. Programmer
    8. Exit
    """)

    opt = input("Enter the operation of your choice(1-8): ")
    if not opt.isdigit():
        print("That is not a valid character. Please input a integer between 1 and 7")
        time.sleep(2)
        continue

    opt_int = int(opt)
    if opt_int < 1 or opt_int > 8:
        print("That is not a valid option! Please input a option of your choice that is in between 1 and 7!")
    elif opt_int == 8:
        for wait_time in range(4):
            print("Exiting" + "." * count)
            count += 1
            time.sleep(0.69)
        time.sleep(random.randint(0, 3))
        break
    elif opt_int == 7:
        while True:
            while True:
                try:
                    num_type = int(input("Enter the number type (1. Decimal/2. Binary/3. Hexadecimal): "))
                    break
                except ValueError:
                    print("That is not a valid option. Please input a number between 1 and 3.")
                    time.sleep(2)
                    continue
            if num_type < 1 or num_type > 3:
                print("That is not a valid option. Please input a number between 1 and 3. ")
                time.sleep(2)
                continue

            if num_type == 1:
                dec = int(input("Enter your decimal (base 10) number: "))
                dec_bin = bin(dec)
                dec_hex = hex(dec)
                print(f"""
                Dec -> Bin: {dec_bin}
                Dec -> Hex: {dec_hex}
    """)

            if num_type == 2:
                while True:
                    try:
                        bina = input("Enter your binary (base 2) number: ")
                        break
                    except ValueError:
                        print("Please enter a binary number!")
                        time.sleep(2)
                        continue
                bina_dec = int(bina, 2)
                bina_hex = hex(bina_dec)
                print(f"""
                Bin -> Dec: {bina_dec}
                Bin -> Hex: {bina_hex}
    """)

            if num_type == 3:
                hexa = input(
                    "Enter your hexadecimal (base 16) number (Include 0x at the start and use capital letters): ")
                hexa_dec = int(hexa, 16)
                hexa_bin = bin(hexa_dec)
                print(f"""
                Hex -> Dec: {hexa_dec}
                Hex -> Bin: {hexa_bin}
    """)
            question_p = input("Do you want to calculate again? (y/n): ")
            if question_p == "y":
                continue
            else:
                break

    elif opt_int == 6:
        while True:
            try:
                num1 = float(input("Enter your first number: "))
                break
            except ValueError:
                print("That is not a number! Please input a decimal or a whole non-negative number!")
                time.sleep(2)
                continue
        print(f"The square root of {num1} is {round(sq_ro(num1), 4)} \n")
        question_s = input("Do you want to calculate again?(y/any key to exit): ")
        if question_s.lower() == "y":
            continue
        else:
            for wait_time in range(4):
                print("Exiting" + "." * count)
                count += 1
                time.sleep(0.69)
            time.sleep(random.randint(0, 3))
            break
    else:
        while True:
            try:
                num1 = float(input("Enter your first number: "))
                break
            except ValueError:
                print("That is not a number. Please enter a number.")
                time.sleep(2)
        while True:
            try:
                num2 = float(input("Enter your second number: "))
                break
            except ValueError:
                print("That is not a number. Please enter a number.")
                time.sleep(2)

        if opt_int == 1:
            print(f"The sum of {num1} and {num2} is {add(num1, num2)} \n")
        elif opt_int == 2:
            print(f"The difference of {num1} and {num2} is {sub(num1, num2)} \n")
        elif opt_int == 3:
            print(f"The product of {num1} and {num2} is {mul(num1, num2)} \n")
        elif opt_int == 4:
            try:
                print(f"The quotient of {num1} and {num2} is {divide(num1, num2)} \n")
            except ZeroDivisionError:
                print("Division by Zero is not possible!")
                time.sleep(2)
                continue
        elif opt_int == 5:
            print(f"{num1} raised to the power of {num2} is {expo(num1, num2)} \n")
        question = input("Do you want to calculate again?(y/any key to exit): ")
        if question.lower() == "y":
            continue
        else:
            for wait_time in range(4):
                print("Exiting" + "." * count)
                count += 1
                time.sleep(0.69)
            time.sleep(random.randint(0, 3))
            break
