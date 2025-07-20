import random
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class CoreGame:
    def __init__(self,score,difficulty,operation_choice,high_score):
        self.score = score
        self.difficulty = difficulty
        self.operation_choice = operation_choice
        self.high_score = high_score
    
    def modify_score(self,modifier):
        self.score = self.score + modifier

    def get_score(self):
        return self.score
    
    def chk_score(self):
        global num_question 
        if self.score <= 0:
            messagebox.showinfo("Game",f"You lost! Your high score was: {self.high_score}")
            num_question = 0

    def print_factors(self, x):
        factors = []
        for i in range(1,x+1):
            if self.difficulty.upper() in ("E","M"):
                if x%i==0:
                    if i < 10:
                        factors.append(i)
            elif self.difficulty.upper() == "H":
                for i in range(1,x+1):
                    if x%i==0:
                        if i > 10:
                            factors.append(i)
        if len(factors) == 0:
            return self.numa()
        else:
            return random.choice(factors)
            

    def numa(self):
        global a
        if self.difficulty.upper() == "E":
            a = random.randint(1, 9)
        elif self.difficulty.upper() in ("M","H"):
            a = random.randint(10,99)
        return a

    # def geta(self):
    #     return a
    
    def numb(self):
        global b

        factor = self.print_factors(a)
        if self.operation_choice in ("add","mul"):
            if self.difficulty.upper() in ("E","M"):
                b = random.randint(1, 9)
            elif self.difficulty.upper() == "H":
                b = random.randint(10, 99)
        elif self.operation_choice == "sub":
            if self.difficulty.upper() in ("E","H"):
                b = random.randint(1, a)
            elif self.difficulty.upper() == "M":
                b = random.randint(1, 9)
        elif self.operation_choice == "div":
#            b = random.randint(1,random.choice(factor))
            b = random.choice(factor)
        return b
    
    # def getb(self):
    #     return b
    def chk_answer(self,is_correct):
            if is_correct:
                self.modify_score(1)
                messagebox.showinfo("Result",f"Correct, you earned one point! Your score is: {self.get_score()}")
                set_high_score()
            else:
                self.modify_score(-1)
                messagebox.showinfo("Result",f"Incorrect, you earned lost a point. Your score is: {game.get_score()}")
                self.chk_score()

tk = Tk()
tk.title("Math Game")
tk.geometry("800x600")
score = 0
high_score = 0

def set_high_score():
    if game.score > game.high_score:
        game.high_score = game.score

def start_game():
    global game
    global num_question
    level = simpledialog.askstring("Difficulty", "Easy (E), Medium (M), or Hard (h)")
    num_question = simpledialog.askinteger("Amount","How much questions do you want to be quizzed on?: ")
    
    def ask_questions():
        global game
        operations = ["div"]
        operation = random.choice(operations)       
        game = CoreGame(score,level,operation,high_score)
        global num_question
        if num_question > 0:
            if game.operation_choice == "add":
                numa = game.numa()
                numb = game.numb()
                answer_a = numa+numb
                guess_a = simpledialog.askinteger("Guess", f"What is {numa} + {numb}: ")
                if guess_a == answer_a:
                    game.chk_answer(True) 
                else:
                    game.chk_answer(False)
            elif game.operation_choice == "sub":
                numa = game.numa()
                numb = game.numb()
                answer_s = numa-numb
                guess_s = simpledialog.askinteger("Guess", f"What is {numa} - {numb}: ")
                if guess_s == answer_s:
                    game.chk_answer(True) 
                else:
                    game.chk_answer(False)
            tk.after(100, ask_questions)
            num_question -= 1
    ask_questions()
    print(game.high_score)


start_btn = Button(tk,text="Start Game",command=start_game)
start_btn.pack()

exit_btn = Button(tk,text="Exit",command=tk.destroy)
exit_btn.pack()

tk.mainloop()
