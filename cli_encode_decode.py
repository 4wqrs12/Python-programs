import time
import random

print("""
Text encrypter/decrypter V1
""")

while True:

    count = 0

    opt = input("Do you want to encrypt(e) or decrypt(d) a string, or exit(x)?: ")

    if opt.lower() != "e" and opt.lower() != "d" and opt.lower() != "x":
        print("Please enter \"e\", \"d\" or \"x\" ")
    else:

        if opt.lower() == "e":
            string = input("Enter the string to encrypt: ")

            if string == " ":
                print("Please enter a string.")
            else:
                string_reversed = reversed(string)

                print("The encrypted string is: ")
                for chars in string_reversed:
                    encrypt = ord(chars)
                    print(encrypt, end=" ")
                print(" ")
        elif opt.lower() == "d":
            integers = []
            decrypts = []

            # Get integers
            while True:
                while True:
                    try:
                        integer = int(input("Enter the integers from left to right, enter \"256\" once you are finished: "))
                        print(" ")
                        # integer = int(input("Enter the integers from right to left, enter \"256\" once you are finished: "))
                        break
                    except ValueError:
                        print("Please enter an integer!")
                        continue
                if integer > 256 or integer < 0:
                    print("Please enter a number between 0 and 256! (Including both endpoints)")
                integers.append(integer)

                if integer == 256:
                    integers.remove(256)
                    for nums in integers:
                        decrypt = chr(nums)
                        decrypts.append(decrypt)
                    reversed_decrypts = list(reversed(decrypts))


                    print("The decrypted string is: ")
                    for decrypt_da_list in reversed_decrypts:
                        print(decrypt_da_list, end="")
                    print(" ")
                    break
        elif opt.lower() == "x":
            for wait_time in range(4):
                print("Exiting"+"."*count)
                time.sleep(0.69)
                count += 1
            time.sleep(random.randint(1, 3))
            break

    question = input("Do you want to continue? \"Y\" to run again, or any key to exit: ")
    if question.lower() == "y":
        continue
    else:
        for wait_time in range(4):
            print("Exiting"+"."*count)
            time.sleep(0.69)
            count += 1
        time.sleep(random.randint(1, 3))
