import random
import tkinter as Tk
import quotes
technobladequote = random.choice(quotes.quoter)
def printquote():
    ggg = len(technobladequote)
    if ggg >= 30:
        iflong = 18
    else:
        iflong = 6
    label = Tk.Label(None, text=technobladequote, font=('Times', iflong),fg='black')
    label.pack()
    label.mainloop()
printquote()