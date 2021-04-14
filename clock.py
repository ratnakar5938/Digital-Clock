from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def getTime():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, getTime)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center", expand=True)

getTime()

mainloop()