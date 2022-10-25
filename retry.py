import random
import tkinter as Tk
import quotes
technobladequote = random.choice(quotes.quoter)
def printquote():
    ggg = len(technobladequote)
    if ggg >= 30:
        iflong = 6
    else:
        iflong = 18
    label = Tk.Label(None, text=technobladequote, font=('Times', iflong),fg='black')
    label.pack()
    label.mainloop()
printquote()
