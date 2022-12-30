import keyboard
import os
import random
from tkinter import *
root = Tk()
if 'hotkey.txt' in os.listdir():
    f = open("hotkey.txt", "r")
else:
    print('choose a hotkey')
    g = input()
    h = open("hotkey.txt", "w")
    h.write(g)
    f = open("hotkey.txt", "r")
hotkey = f.read()
if 'quitkey.txt' in os.listdir():
    ff = open("quitkey.txt", "r")
else:
    print('choose a quitkey')
    gg = input()
    hh = open("quitkey.txt", "w")
    hh.write(gg)
    ff = open("quitkey.txt", "r")
quitkey = ff.read()
import quotes
technobladequote = random.choice(quotes.quoter)
def printquote():
	w = Label(root, text=technobladequote)
	w.pack()
	root.mainloop()
keyboard.add_hotkey(hotkey, printquote, args = ())
keyboard.wait(quitkey)
