info = {}
count = int(input("How much full names will be entered?: "))
num = 0 
for i in range(count):
    f = input("Enter your first name: ")
    l = input("Enter your last name: ")
    info[f] = l

first = list(info.keys())
last = list(info.values())


print("""
    First Name | Last Name
    ----------------------
    """)
for j in range(count):
    test = f"{first[num]} | {last[num]}"
    print(f"""
    {test.center(15)}
    """)
    num += 1
