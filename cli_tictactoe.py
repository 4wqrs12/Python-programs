print("""
Python Tic-Tac-Toe
""")



game_dic = {1: "1", 2: "2", 3: "3",
            4: "4", 5: "5", 6: "6",
            7: "7", 8: "8", 9: "9"}
print("Player 1: X, Player 2: O")

def get_board():
    game_board = f"""
    |{game_dic[1]}|{game_dic[2]}|{game_dic[3]}|
    |{game_dic[4]}|{game_dic[5]}|{game_dic[6]}|
    |{game_dic[7]}|{game_dic[8]}|{game_dic[9]}|
    """
    print(game_board)

def check_draw(d):
    draw = []

    for value in d.values():
        draw.append(value)

    string = "".join(draw)
    if string.isalpha():
        print("Draw!")
        exit()

wins_horiz = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
wins_vert = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
wins_diag = [(1, 5, 9), (3, 5, 7)]

def check_winner(s):
    for i in wins_horiz+wins_vert+wins_diag:
        if game_dic[i[0]] == s and game_dic[i[1]] == s and game_dic[i[2]] == s:
            return True
    return False
player_1_draw = []

while True:

    while True:
        opt_1 = input("Player 1, enter which number you are going to pick: ")

        if int(opt_1) < 1 or int(opt_1) > 9:
            print("Please enter a valid number!")
            continue
        else:
            if game_dic[int(opt_1)] == "O" or game_dic[int(opt_1)] == "X":
                print("Please choose another number, this one is chosen!")
                continue
            else:
                game_dic[int(opt_1)] = "X"
                get_board()

        if check_winner("X"):
            print("Player 1 wins!")
            exit()

        check_draw(game_dic)
        break
    
    while True:
        opt_2 = input("Player 2, enter which number you are going to pick: ")

        if int(opt_2) < 1 or int(opt_2) > 9:
            print("Please enter a valid number!")
            continue
        else:
            if game_dic[int(opt_2)] == "O" or game_dic[int(opt_2)] == "X":
                print("Please choose another number, this one is chosen!")
                continue
            else:
                game_dic[int(opt_2)] = "O"
                get_board()
                

        

        if check_winner("O"):
            print("Player 2 wins!")
            exit()

        check_draw(game_dic)
        break
