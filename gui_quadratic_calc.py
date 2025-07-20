from tkinter import * 
from tkinter import messagebox
from tkinter import simpledialog


tk = Tk()
tk.geometry("800x600")
tk.title("Quadratic Equation Calculator")

def round_complex(x):
    return complex(round(x.real),round(x.imag))


def close():
    exit()

def solve_quadratic():
    a = simpledialog.askfloat("Term A","Enter term A: ")
    b = simpledialog.askfloat("Term B","Enter term B: ")
    c = simpledialog.askfloat("Term C","Enter term C: ")

    try:  
        new_b = -1*b
        dis = (b**2 - 4*a*c)**0.5
        deno = 2*a

        root1 = (new_b + dis) / (deno)
        root2 = (new_b - dis) / (deno)

        if isinstance(root1,complex) and isinstance(root2,complex):
            messagebox.showinfo("Answer",f"Root 1: {round(round_complex(root1),4)}, Root 2: {round(round_complex(root2),4)}")
        elif isinstance(root2,complex):
            messagebox.showinfo("Answer",f"Root 1: {round(root1,4)}, Root 2: {round(round_complex(root2),4)}")
        elif isinstance(root1,complex):
            messagebox.showinfo("Answer",f"Root 1: {round(round_complex(root1),4)}, Root 2: {round(root2,4)}")
        else:
            messagebox.showinfo("Answer",f"Root 1: {round(root1,4)}, Root 2: {round(root2,4)}")


    except TypeError:
        messagebox.showwarning("Error","Please enter a number for Term A, B, and C!") 
     

solve = Button(tk,text="Solve Quadratic Equation",command=solve_quadratic)
solve.pack()


quit = Button(tk,text="Quit",command=close)
quit.pack()


tk.mainloop()
