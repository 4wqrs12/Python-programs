from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
is_player_X = True
gamesquare_dict = {}
wins_horiz = [("00","01","02"),("10","11","12"),("20","21","22")]
wins_vert = [("00","10","20"),("01","11","21"),("02","12","22")]
wins_diag = [("00","11","22"),("02","11","20")]
class GameSquare:
    def __init__(self,row_amount,column_amount,player=None):
        self.player = player
        self.player_btn = Button(tk,text=self.player,command=self.player_turn_display)
        self.player_btn.grid(row=row_amount,column=column_amount)
        self.player_btn.configure(width=10,height=5)

    def get_btn_text(self):
        return self.player_btn.cget('text')

    def get_row(self):
        return self.player_btn.grid_info()["row"]

    def get_column(self):
        return self.player_btn.grid_info()["column"]
    
    def player_turn_display(self):
        global is_player_X
        print(self.get_row())
        print(self.get_column())
        if is_player_X and self.player_btn["text"] == "":
            print("Player O turn")
            player_turn.set("Player O turn. ")
            self.player_btn["text"] = "X"
            if check_winner("X"):
                messagebox.showinfo("Winner","Player X won the game. ")
                tk.destroy()
            else:
                check_draw()
            is_player_X = False
            check_draw()
        elif is_player_X == False and self.player_btn["text"] == "":
            print("Player X turn")
            player_turn.set("Player X turn. ")
            check_draw()
            self.player_btn["text"] = "O"
            if check_winner("O"):
                messagebox.showinfo("Game","Player O won the game. ")
                tk.destroy()
            else:
                check_draw()
            is_player_X = True

def make_gameboard():
    global gamesquare
    for row in range(3):
        for col in range(3):
            gamesquare = GameSquare(row,col)
            gamesquare_dict[f"{row}{col}"] = gamesquare

def check_winner(p):
    for i in wins_horiz+wins_vert+wins_diag:
        if gamesquare_dict[i[0]].get_btn_text() == p and gamesquare_dict[i[1]].get_btn_text() == p and gamesquare_dict[i[2]].get_btn_text() == p:
            return True
    return False

def check_draw():
    global draw_length
    draw = []

    draw_length = len(draw)

    for v in gamesquare_dict.values():
        draw.append(v.get_btn_text())

    if "" not in draw:
        messagebox.showinfo("Game","It is a draw. ")
        tk.destroy()


tk = Tk()
tk.resizable(False, False)
player_turn = StringVar()

tk.title("Tic-Tac-Toe")
make_gameboard()
player_turn.set("Player X turn. ")
player_turn_lbl_frame = Frame(tk,width=100,height=100)
player_turn_lbl_frame.grid(row=6,column=6)
player_turn_lbl = Label(player_turn_lbl_frame,textvariable=player_turn)
player_turn_lbl.grid(row=6,column=6)
tk.mainloop()
