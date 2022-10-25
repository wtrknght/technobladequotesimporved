import random
import tkinter as Tk
import quotes
import keyboard
keyboard.add_hotkey("e", lambda: printquote())
technobladequote = random.choice(quotes.quoter)
def printquote():
    ggg = len(technobladequote)
    if ggg >= 30:
        iflong = 12
    elif ggg >= 1000:
        iflong = 3
    else:
        iflong = 18
    label = Tk.Label(None, text=technobladequote, font=('Times', iflong),fg='black')
    label.pack()
    label.mainloop()
printquote()
