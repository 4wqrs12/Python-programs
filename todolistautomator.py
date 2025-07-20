import pyautogui
import time
separator = "-----------"
day = input("What dae: Monday (M), Tuesday (T), Wednesday (W), Thursday (Th), Friday (F): ").lower()
date = input("Enter the date (Ex: 6/8/11): ")
title_text = f'''
{date}
{separator}
'''
screen_width, screen_height = pyautogui.size()
current_x, current_y = pyautogui.position()
def get_pos():
    return pyautogui.position()
pos = get_pos()
print(pos)

def open_notes(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def goto_main_todolist():
    pyautogui.moveTo(99,89)
    pyautogui.click()

def scroll_down():
    pyautogui.moveTo(1592,73)
    pyautogui.mouseDown()
    while get_pos() != (1584,895):
        pyautogui.dragTo(1584, 895, button='left')
    pyautogui.mouseUp()

def go_to_day():
    # For each case, make it one-liner
    if day == "m":
        pyautogui.moveTo(54,363)
        pyautogui.click()
    elif day == "t":
        pyautogui.moveTo(76,258)
        pyautogui.click()
    elif day == "w":
        pyautogui.moveTo(119,149)
        pyautogui.click()
    elif day == "th":
        pyautogui.moveTo(105,335)
        pyautogui.click()
    else:
        pyautogui.moveTo(79,204)
        pyautogui.click()

def highlight():
    pyautogui.moveTo(256,153)
    pyautogui.mouseDown()
    pyautogui.dragTo(481,732, 2, button='left')

def copy_text():
    pyautogui.rightClick()
    pyautogui.moveTo(524,521)
    time.sleep(0.5)
    pyautogui.click()


def paste_text():
    pyautogui.rightClick()
    pyautogui.moveTo(384,572)
    time.sleep(0.5)
    pyautogui.click()

def keyboard_operation(key, amount):
    pyautogui.press(key,presses=amount)


open_notes(520,863)
time.sleep(2)
goto_main_todolist()
go_to_day()
highlight()
copy_text()
time.sleep(2)
goto_main_todolist()
scroll_down()
pyautogui.click(259,817)
time.sleep(1.5)
keyboard_operation("backspace",1)
keyboard_operation("enter",4)
pyautogui.typewrite(title_text)
paste_text()