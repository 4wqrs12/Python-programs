import random
import time

objs = []

while True:
    count = 0

    obj = input("Enter something into the wheel spinner, enter '~' to finish: ")
    objs.append(obj)

    if obj == "~":
        objs.remove("~")
        get_random_obj = random.choice(objs)
        print(f"The winner is:")
        for wait in range(4):
            print("Choosing"+"."*count)
            count += 1
            time.sleep(2)
        time.sleep(1)
        print(f"{get_random_obj} !")
        break
