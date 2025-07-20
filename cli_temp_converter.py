print("""
Temp Converter
""")

while True:
    temp_type = input("Enter if your temperature is in either celsius or farenhiet (C or F): ")

    if temp_type != "C".upper() and temp_type != "F".upper():
        print("That is not an option!")
    else:
        if temp_type == "F".upper():
            while True:
                try:
                    f = float(input("Enter the temperature in fahrenheit: "))
                    break
                except ValueError:
                    print("Please enter a number or decimal!")
                    continue
            celsius = ((f-32)*5)/9
            print(f"{f} F to celsius is: {round(celsius, 4)}")
        elif temp_type == "C".upper():
            while True:
                try:
                    c = float(input("Enter the temperature in celsius: "))
                    break
                except ValueError:
                    print("Please enter a number or decimal")
                    continue
            farenheit = ((c*9/5)+32)
            print(f"{c} C to farenheit is: {round(farenheit, 4)}")
        else:
            print("How did you get this message?")
    question = input("Do you want to calculate again?(y/n): ")
    if question == "y":
        continue
    else:
        break
