from tkinter import *
import time

#akna seaded
aken = Tk()
aken.title('Animatsioon')
aken.iconbitmap('kappa.ico')

#lõuendi loomine
louend = Canvas(aken, width=250, height=250)
louend.pack()

#palli lisamine
pall = louend.create_oval(115,115,125,125, fill="black")

#funktsioon palli liigutamiseks
def liiguta_objekti(event):
    for x in range(0,20):
        louend.move(pall,5,5)
        aken.update()
        time.sleep(0.05)

#reageerimine klaviatuurile
louend.bind_all('<KeyPress-Return>', liiguta_objekti )

aken.mainloop()