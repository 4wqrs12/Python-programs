from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog



# Game info for player and buildings
py_info = {
    "name": "Py",
    "count": 0
}

oldpy_info = {
    "name": "Old Py",
    "count": 0,
    "multiplier": 2,
    "cost": 5
}

workerpy_info = {
    "name": "Worker Py",
    "count": 0,
    "multiplier": 4,
    "cost": 7
}

templepy_info = {
    "name": "Py Temple",
    "count": 0,
    "multiplier": 6,
    "cost": 9
}

rocketpy_info = {
    "name": "Rocket Py",
    "count": 0,
    "multiplier": 10,
    "cost": 14
}

# Functions
def update_handler(dict_name,not_py=None):
    # Only for manually clicking the py
    if not_py == None:
        # Incremeting the money of the py
        py_info["count"] += 1
        # Debugging
        print(f"Incrementing manually: {py_info['count']}")
        # Connect the display_pys to the py_info dictionary, specifically the "count" key
        display_pys.set(f"Pys: {py_info['count']}")
    # If not clicking manually, then buildings would go to this case
    elif not_py:
        # Debugging
        print("In not_py")
        # Deduct money, if there is enough money
        if py_info["count"] >= dict_name["cost"]:
            # Debugging
            print("In money checker")
            # Increase the amount of buildings we have for a building
            dict_name["count"] += 1
            # Debugging
            print(f"Buildings: {dict_name['count']}")
            # Here we deduct money if above condition is True
            py_info["count"] -= dict_name["cost"]*dict_name["count"]
            if py_info["count"] < 0:
                display_pys.set(f"Pys: 0")
            else:
                display_pys.set(f"Pys: {py_info['count']}")
            # Debugging
            print(f"After Deduction: {py_info['count']}")
            # Connect the display_pys to the py_info dictionary, specifically the "count" key
            if dict_name["count"] > 0:
                # Debugging
                print(f"There is {dict_name['count']} buildings:")
                # Nested function for buildings to autmatically update the pys, doing this won't decrease the pys every second 
                def auto_updater():
                    # Debugging
                    print(f"What it is incremeting automatically by: {dict_name['multiplier']*dict_name['count']}, {dict_name['name']}")
                    # Increment the pys by the mutliplier of the building mulitplied by how much of that building that they have
                    py_info["count"] += dict_name["multiplier"]*dict_name["count"]
                    # Update pys constantly
                    tk.after(1000,auto_updater)
                    # Display the new pys after change
                    display_pys.set(f"Pys: {py_info['count']}")
                auto_updater()
        else:
            # If the "if" condition is False, then use messagebox to tell the user that they do not have enough money for the purchase
            messagebox.showwarning("Warning","You do not have enough money to purchase this item!")

def get_info_func(dict_name,x,y,anchor_type,parent):
    display_info = StringVar()
    display_info.set(F"You have {dict_name['count']} {dict_name['name']}(s). It costs: {dict_name['cost']} Pys.")
    # Debugging
    # print(f"Count: {dict_name['count']}, name: {dict_name['name']}")
    info = Label(parent,textvariable=display_info)
    info.place(relx=x,rely=y,anchor=anchor_type)
    tk.after(100,lambda: get_info_func(dict_name,x,y,anchor_type,parent))

def close():
    exit()

def sell_handler():
    sell_opt = simpledialog.askstring("Choose what to sell","o (Old Py), w (Worker Py), t (Py Temple), r (Rocket Py)")
    if sell_opt.lower() == "o":
        print("Selling o")
        amounto = simpledialog.askinteger("Count","How much old pys do you want to sell?")
        if amounto <= oldpy_info["count"]:
            oldpy_info["count"] -= amounto
            py_info["count"] += amounto*oldpy_info["multiplier"]
            display_pys.set(f"Pys: {py_info['count']}")
        elif amounto > oldpy_info["count"]:
            messagebox.showerror("Error","You do not have enough old pys!")
    elif sell_opt.lower() == "w":
        print("Selling w")
        amountw = simpledialog.askinteger("Count","How much worker pys do you want to sell?")
        if amountw <= workerpy_info["count"]:
            workerpy_info["count"] -= amountw
            py_info["count"] -= amountw*workerpy_info["multiplier"]
            display_pys.set(f"Pys: {py_info['count']}")
        elif amountw > oldpy_info["count"]:
            messagebox.showerror("Error","You do not have enough worker pys!")
    elif sell_opt.lower() == "t":
        print("Selling t")
        amountt = simpledialog.askinteger("Count","How much py temples do you want to sell?")
        if amountt <= templepy_info["count"]:
            templepy_info["count"] -= amountt
            py_info["count"] -= amountt*templepy_info["multiplier"]
            display_pys.set(f"Pys: {py_info['count']}")
    elif sell_opt.lower() == "r":
        print("Selling r")
        amountr = simpledialog.askinteger("Count","How much py rockets do you want to sell?")
        if amountr <= rocketpy_info["count"]:
            rocketpy_info["count"] -= amountr
            py_info["count"] -= amountr*rocketpy_info["multiplier"]
            display_pys.set(f"Pys: {py_info['count']}")
    else:
        messagebox.showwarning("Warning","Please enter a valid option!")

# Window setup
tk = Tk()
tk.title("PyClicker")
tk.geometry("1200x1200")

# Setting variables to display things
display_pys = IntVar()

# Get the images
py_image = PhotoImage(file="py.png")
oldpy_image = PhotoImage(file="oldpy.png")
workerpy_image = PhotoImage(file="workerpy.png")
templepy_image = PhotoImage(file="templepy.png")
rocketpy_image = PhotoImage(file="rocketpy.png")
# Windows
# C:\\Users\\MayurS\\Downloads\\coding-projects-main\\coding-projects-main\\py.png
# C:\\Users\\MayurS\\Downloads\\coding-projects-main\\coding-projects-main\\oldpy.png
# C:\\Users\\MayurS\\Downloads\\coding-projects-main\\coding-projects-main\\workerpy.png

# hacOS
# /Users/mayur/coding-projects/py.png
# /Users/mayur/coding-projects/oldpy.png
# /Users/mayur/coding-projects/workerpy.png

# Setting up the buttons
py_button = Button(tk,image=py_image,command=lambda: update_handler(py_info,None))
py_button.place(relx=0.5,rely=0.5,anchor=CENTER)

oldpy_button = Button(tk,image=oldpy_image,command=lambda: update_handler(oldpy_info,True))
oldpy_button.place(relx=0.95,rely=0.11,anchor=CENTER)
# Old Py label
get_info_func(oldpy_info,0.9,0.2,CENTER,tk)


workerpy_button = Button(tk,image=workerpy_image,command=lambda: update_handler(workerpy_info,True))
workerpy_button.place(relx=0.97,rely=0.3,anchor=CENTER)
# Worker Py label
get_info_func(workerpy_info,0.89,0.35,CENTER,tk)

templepy_button = Button(tk,image=templepy_image,command=lambda: update_handler(templepy_info,True))
templepy_button.place(relx=0.965,rely=0.45,anchor=CENTER)
# Temple Py label
get_info_func(templepy_info,0.89,0.5,CENTER,tk)

rocketpy_button = Button(tk,image=rocketpy_image,command=lambda: update_handler(rocketpy_info,True))
rocketpy_button.place(relx=0.93,rely=0.65,anchor=CENTER)
# Rocket Py label
get_info_func(rocketpy_info,0.89,0.7,CENTER,tk)

quit_game = Button(tk,text="Quit Game",command=close)
quit_game.place(relx=0.5,rely=0.95,anchor=CENTER)

sell_btn = Button(tk,text="Sell Buildings",command=sell_handler)
sell_btn.place(relx=0.93,rely=0.85,anchor=CENTER)

# Display the amount of pys the user has
get_pys = Label(tk,textvariable=display_pys)
get_pys.place(relx=0.5,rely=0.75,anchor=CENTER)


tk.mainloop()
