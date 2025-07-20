while True:
    n = int(input("Enter a integer: "))
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
            steps += 1
            print(n)
        elif n % 2 == 1:
            n = (n * 3) + 1
            steps += 1
            print(n)

    print(f"Steps: {steps}")

    question = input("Continue? (y/n): ")
    if question.lower() == "y":
        continue
    break
