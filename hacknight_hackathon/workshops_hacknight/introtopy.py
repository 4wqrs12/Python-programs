board = [[".",".",".",".",".",".","."],
         [".",".",".",".",".",".","."],
         [".",".",".",".",".",".","."],
         [".",".",".",".",".",".","."],
         [".",".",".",".",".",".","."],
         [".",".",".",".",".",".","."]]
def get_board():
    print("0123456")
    for row in board:
        for col in row:
            print(col,end="")
        print()

def drop_piece(col,piece):
    for row in range(5,-1,-1):
        if board[row][col] == ".":
            board[row][col] = piece
            return row

def is_droppable(col):
    if col < 1 or col > 7:
        return False
    
    if board[0][col-1] != ".":
        return False
    
    return True


def play_turn(name,piece):
    get_board()
    print(f"{name}, it is your turn. Your are {piece}. ")

    # Asks user for a column
    col = int(input("Enter a column: "))
    while not is_droppable(col):
        col = int(input("Invalid column. Please enter a new one: "))

    row = drop_piece(col,piece)
    return check_win(row,col)

def check_win(row,col):
    if row < 3:
        if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
            return True
    for i in range(4):
        if board[row][i] == board[row][i+1] == board[row][i+2] == board[row][i+3]:
            if board[row][i] != ".":
                return True
    if row < 3:
        for i in range(4):
            if board[row][i] == board[row+1][col] == board[row+2][i+2] == board[row+3][i+3]:
                if board[row][i] != ".":
                    return True
                
        for i in range(3,7):
            if board[row][i] == board[row+1][col] == board[row+2][i+2] == board[row+3][i+3]:
                        if board[row][i] != ".":
                            return True
    return False
def play_game():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    while True:
        if play_turn(player1,"x"):
            get_board()
            print(f"{player1} has won the game!")
            break
        if play_turn(player2,"o"):
            get_board()
            print(f"{player2} has won the game!")
            break

play_game()