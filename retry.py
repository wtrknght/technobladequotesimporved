import random
import tkinter as Tk
import quotes
import sys
import keyboard
try:
    f = open("hotkey.txt", "r")
except:
    print('choose a hotkey')
    g = input()
    ddd = open("hotkey.txt", "x")
    h = open("hotkey.txt", "w")
    h.write(g)
    f = open("hotkey.txt", "r")
hotkey = f.read()
try:
    ff = open("quitkey.txt", "r")
except:
    print('choose a quitkey')
    gg = input()
    dddd = open("quitkey.txt", "x")
    hh = open("quitkey.txt", "w")
    hh.write(gg)
    ff = open("quitkey.txt", "r")
quitkey = ff.read()
keyboard.add_hotkey(f, lambda: printquote())
keyboard.add_hotkey(ff, lambda: sys.exit())
technobladequote = random.choice(quotes.quoter)
def printquote():
    ggg = len(technobladequote)
    match ggg:
    case 30 => ggg:
         iflong = 12
    case 1000 => ggg:
         iflong = 3
    case _:
         iflong = 18
    label = Tk.Label(None, text=technobladequote, font=('Times', iflong),fg='black')
    label.pack()
    label.mainloop()
printquote()
