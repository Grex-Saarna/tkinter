from tkinter import *
from tkinter import filedialog

win=Tk()
win.geometry("500x500")

Label(win, text="ava", font='Arial 16 bold').pack(pady=15)

def open_file():
    list = []

    silt = Label(win, text="")
    silt.pack()

    filepath = filedialog.askopenfilename(title="ava fail", filetypes=(("text files","*.txt"), ("all files","*.*")))

    with open (filepath) as file:
        file1 = [i for i in file.read().strip().split("\n")]

    for i in file1:
        if float(i) > float(0):
            list.append(float(i))
    
    silt.config(text=list)

button = Button(win, text="Open", command=open_file).pack()

win.mainloop()