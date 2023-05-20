import tkinter as tk
import random


def counting(x):
    total = 0
    for l in x:
        total += 1
    x.seek(0)
    return total


root = tk.Tk()
fh = open('phrases.txt', 'r')
root.minsize(640, 460)
label = tk.Label(root, text=None)


def genline(x):
    print("Click")
    a = random.randint(1, counting(x))
    count = 0
    for l in fh:
        count += 1
        if count == a:
            label.config(text=l)


def rndz():
    print(random.randint(1, counting(fh)))


button = tk.Button(text="Click me!", width=30, height=10, bg='black', fg='red', command=rndz()).pack()

label.pack()

root.mainloop()
