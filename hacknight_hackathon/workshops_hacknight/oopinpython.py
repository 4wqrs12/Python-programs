from tkinter import *
import random

class MSCell(Label):
    def __init__(self,master,location):
        Label.__init__(self,master,height=1,width=2,text="",bg="white",font=("Arial", 24),relief=RAISED)
        self.location = location
        self.exposed = False
        self.flagged = False
        self.value = "blank"

        self.bind("<Button-1>",self.expose)
    def get_value(self):
        return self.value

    def set_value(self,val):
        self.value = val

    def update_cell(self):
        if self.exposed:
            self["relief"] = SUNKEN
            self["bg"] = "lightgray"

            if self.value == "blank":
                self["text"] = ""
            elif self.value != "bomb":
                self["text"] = str(self.value)
            else:
                self["text"] = "b"
                self["bg"] = "red"
        elif self.flagged:
            self["text"] = "f"
        else:
            self["text"] = ""
    
    def expose(self,event):
        if self.exposed:
            return
        if self.flagged:
            return
        self.exposed = True
        self.update_cell()
    

class MSGrid(Frame):
    def __init__(self,master,height,width,num_bombs):
        Frame.__init__(self,master,bg="black")
        self.grid()

        # attrs
        self.height = height
        self.width = width
        self.num_bombs = num_bombs

        for i in range(1,height*2-1,2):
            self.rowconfigure(i,minsize=1)

        for i in range(1,width*2-1,2):
            self.columnconfigure(i,minsize=1)

        self.cells = {}
        for row in range(height):
            for col in range(width):
                self.cells[(row, col)] = MSCell(self,(row,col))
                self.cells[(row,col)].grid(row=2*row,column=2*col)
        self.add_bombs(num_bombs) 
    def add_bombs(self,num):
        for i in range(num):
            row, col = random.randrange(0,self.height),random.randrange(0,self.width)
        while self.cells[(row,col)].get_value() == "bomb":
            row, col = random.randrange(0,self.height),random.randrange(0,self.width)
        
        self.cells[(row,col)].set_value("bomb")

    




root = Tk()
root.title("Minesweeper")
grid = MSGrid(root,10,12,15)
root.mainloop()