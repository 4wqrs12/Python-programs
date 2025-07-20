from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random

tk = Tk()
tk.geometry("800x600")
tk.resizable(False, False)
tk.configure()
tk.title("Random Number Generator")
get_randint = IntVar()
while True:
    first_endpoint = simpledialog.askinteger("First endpoint","Input first endpoint",parent=tk)
    second_endpoint = simpledialog.askinteger("Second endpoint","Enter the second endpoint",parent=tk)
    if first_endpoint > second_endpoint:
        # display_err = Label(tk, text="The first endpoint must be less than the second endpoint")
        # display_err.pack()
        messagebox.showwarning("Warning","The first endpoint must be less than the second endpoint")
        continue
    break
rand_int = random.randint(first_endpoint,second_endpoint)
get_randint.set(rand_int)
display_text = Label(tk,text="Random Number: ")
display_text.pack()
display_randint = Label(tk,textvariable=get_randint,anchor=CENTER)
display_randint.pack()

tk.mainloop()
