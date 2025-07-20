print("""
TODO List
""")
activites = []
completed_activities = []

num_of_acts = int(input("How much things to do want to complete today?: "))

for main_loop in range(num_of_acts):
    activity = input("Enter the name of the activity that you want to complete today in order: ")
    activites.append(activity)
print()
print("Your activities: ")

for x, y in enumerate(activites):
    print(f"{x+1}. {y}")

while True:
    question = input("Which activities have you completed? (Write the exact name of the activity, type \"~\" when finished): ")

    if question == "~":
        break

    if question not in activites:
        print("Please enter a valid activity!")
    else:
        completed_activities.append(question)


print()
print("Completed activites: ")

for a, b in enumerate(completed_activities):
    print(f"{a+1}. {b}")
