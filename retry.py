import keyboard
import os
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
technobladequote = random.choice(quotes.quoter)
def printquote():
        ggg = len(technobladequote)
        if ggg >= 100:
            iflong = 12
        elif ggg <= 100:
            iflong = 3
        else:
            iflong = 18
        label = Tk.Label(None, text = technobladequote, font = ('Times', iflong),fg = 'black')
        label.pack()
        label.mainloop()
keyboard.add_hotkey(f, printquote, args = ())
keyboard.wait(quitkey)
