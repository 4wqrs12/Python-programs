from tkinter import *
from tkinter import simpledialog
activities_lst = []
class Activity:
    def __init__(self,name):
        self.name = name
        self.check_data = IntVar()
        self.frame = Frame(tk)
        self.check_button = Checkbutton(self.frame, text=self.name, variable=self.check_data, onvalue=1, offvalue=0,command=self.switch)
        self.destroy_btn = Button(self.frame,text="X",fg="red",command=self.destroy_chkbtn)
    

    def destroy_chkbtn(self):
        self.frame.destroy()
        self.check_button.destroy()
        self.destroy_btn.destroy()
    
    def get_name(self):
        return self.name

    def switch(self):
        if self.check_data.get() == 1:
            self.check_button.configure(fg="red")
        else:
            self.check_button.configure(fg="white")

    def pack_lbl(self):
        self.frame.pack()
        self.check_button.pack(side='left')
        self.destroy_btn.pack(side='left')

    def crossout(self):
        if self.check_data.get() == 1:
            print("crossed")
        else:
            print("no")

    def __str__(self):
        return f"{self.name}"
    
def add_item():
    global amount
    opt = simpledialog.askinteger("Add Type", "Do you want to bulk add (1), or add individually (2)?: ")
    if opt == 1:
        amount = simpledialog.askinteger("Amount","How much activities do you want to add?: ")
        def add_activities():
            global amount
            if amount > 0:
                name = simpledialog.askstring("Name","What will be the name of this activity?: ")
                activity = Activity(name)
                activities_lst.append(activity)
                activity.pack_lbl()
                amount -= 1
            tk.after(100,add_activities)
        add_activities()
    elif opt == 2:
        name = simpledialog.askstring("Name","What will be the name of this activity?: ")
        activity = Activity(name)
        activities_lst.append(activity)
        activity.pack_lbl()




tk = Tk()
tk.title("TODO List")
tk.geometry("900x600")
tk.resizable(False, False)


add_btn = Button(tk,text="Add",command=add_item)
add_btn.place(relx=0.01,rely=0.95)


tk.mainloop()
