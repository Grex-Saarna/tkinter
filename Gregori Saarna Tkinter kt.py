#Gregori Saarna
#27.01 2023
#Harjutus 3.3 KT


from tkinter import *
from tkinter import filedialog


win=Tk()
#See teeb akna 500x500
win.geometry("500x500")

#Näitab "Ava" teksti suurust ja fonti
Label(win, text="ava", font='Arial 16 bold').pack(pady=15)

#See avab faili
def open_file():
    list = []

    silt = Label(win, text="")
    silt.pack()
#Sellega valid faili mida avada 
    filepath = filedialog.askopenfilename(title="ava fail", filetypes=(("text files","*.txt"), ("all files","*.*")))

#See avab faili ja siis hakkab kuvama ainult failis olevaid positiivsed numbreid
    with open (filepath) as file:
        file1 = [i for i in file.read().strip().split("\n")]
#Loeb failis olevat sisu
    for i in file1:
        if float(i) > float(0):
            list.append(float(i))
    
    silt.config(text=list)
#Nupp "Open" avab FILE EXPROLERI
button = Button(win, text="Open", command=open_file).pack()

win.mainloop()