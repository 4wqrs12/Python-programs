blank_spaces = []
letters = []
display_number = 0
displays = [
    '''
    o
   /|\\
    |
   / \\
    ''',
    '''
    o
   /|\\
    |
     \\
    ''',
    '''
    o
   /|\\
    |
    ''',
    '''
    o
   /|\\
    ''',
    '''
    o
    |\\
    ''',
    '''
    o
    |
    ''',
    '''
    o
    ''',
    '''
    '''
]



def get_board(string,display_number,part):
    print(displays[display_number])

    if part == "first":
        for i in string:
            blank_spaces.append("_")
            letters.append(i)
    print(" ".join(blank_spaces))
    print()

def guess(guess,display_number,outcome=None):
    global secret_word
    print(display_number)
    if outcome == "correct":
        for i in range(len(letters)):
            if guess == letters[i]:
                blank_spaces[i] = guess
                get_board(secret_word,display_number,"second")



def game():
    global secret_word
    global display_number
    secret_word = input("Enter the secret word: ")
    get_board(secret_word,display_number,"first")

    while True:
        guess_word = input("Enter your guess for a letter: ")
        if guess_word in secret_word:
            guess(guess_word,display_number,"correct")
            if blank_spaces == letters:
                print("You won!")
                break
        else:
            display_number += 1
            if display_number == 7:
                print("You lost!")
                break
            else:
                print("Incorrect!")
                get_board(secret_word,display_number,"second")



game()
