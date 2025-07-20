import time

while True:
    while True:
        try:
            count = int(input("How long would you like your timer to be?(in seconds) : "))
            break
        except ValueError:
            print("Please enter a whole integer number.")
            time.sleep(2)
            continue
    if count < 0:
        print("Please enter a number greater than  or equal to zero!")
    else:
        print(f"Timer set to {count} seconds")

        # for i in range(count):
        #     print(count)
        #     count -= 1
        #     time.sleep(1)
        for x in range(count, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)

        print("TIME'S UP!")

        question = input("Do you want to setup a new timer? (y/or any key to quit): ")
        if question == "y":
            continue
        else:
            break
