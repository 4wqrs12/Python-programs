from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

tk = Tk()
tk.geometry("800x200")
tk.title("Timer")
clock_display = StringVar()

paused = False

def continue_time():
    global paused
    paused = False
    countdown()

def pause():
    global paused
    paused = True


def countdown():
    global count
    if paused == False:
        if count >= 0:
            s = count%60
            m = int(count/60)%60
            h = int(count/3600)
            clock_display.set(f"{h:02}:{m:02}:{s:02}")
            tk.after(1000, countdown)
            count -= 1
        else:
            messagebox.showinfo("Time", "TIMES UP!")
        if paused:
            clock_display.set(f"{h:02}:{m:02}:{s:02}")

def set_time():
    global secs, mins, hrs, count
    count = 0
    secs = simpledialog.askinteger("Seconds","Enter the amount of seconds: ")
    mins = simpledialog.askinteger("Minutes","Enter the amount of minutes: ")
    hrs = simpledialog.askinteger("Hours","Enter the amount of hours: ")
    count = count + hrs * 3600 + mins * 60 + secs

set_btn = Button(tk,text="Set Time",command=set_time)
set_btn.place(relx=0.01,rely=0.01)

start_btn = Button(tk,text="Start",command=countdown)
start_btn.place(relx=0.01,rely=0.15)

stop_btn = Button(tk,text="Stop",command=pause)
stop_btn.place(relx=0.01,rely=0.3)

continue_btn = Button(tk,text="Continue",command=continue_time)
continue_btn.place(relx=0.01,rely=0.45)

clock = Label(tk,textvariable=clock_display,font=("Helvetica", 24))
clock.place(relx=0.45,rely=0.01)

tk.mainloop()
