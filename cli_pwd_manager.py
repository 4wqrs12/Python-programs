print("""
Password Manager
""")

def view(list):
    if len(list) == 0:
        print("You have no passwords stored!")
    else:
        print("Passwords:")
        for j, i in enumerate(list):
            print(f"{j+1}. {i}")

def add(pwd, list):
    list.append(pwd)

def change(list):
    old_pwd = input("Enter the original password: ")
    if old_pwd not in list:
        print(f"{old_pwd} is not an existing password!")
    else:
        loc = list.index(old_pwd)
        new_pwd = input("Enter the new password: ")
        list.remove(old_pwd)
        list.insert(loc, new_pwd)


stored_pwds = []

while True:
    option = input("Do you want to view (v) or add (a) passwords, or change (c) a password?, q to quit: ").lower()
    if option == "q":
        exit()

    if option == "v":
        view(stored_pwds)
    elif option == "a":
        while True:
            password = input("Enter the password that you want to add, hit enter once done: ")
            add(password, stored_pwds)
            if password == "":
                break
        stored_pwds.remove("")
    elif option == "c":
        change(stored_pwds)
    else:
        print(f"{option} is not a valid choice! Please enter \"v\", \"a\", or \"c\".")
        continue
