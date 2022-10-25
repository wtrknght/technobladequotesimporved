import random
import tkinter as Tk
import quotes
technobladequote = random.choice(quotes.quoter)
def printquote():
    ggg = len(technobladequote)
    if ggg >= 200:
        iflong = 12
    elif ggg >= 1000:
        iflong = 3
    else:
        iflong = 18
    label = Tk.Label(None, text=technobladequote, font=('Times', iflong),fg='black')
    label.pack()
    label.mainloop()
printquote()
