from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')

#lõuendi loomine
louend = Canvas(aken, width=400, height=300)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 150,fill="white")
louend.create_rectangle(0, 150, 500, 300,fill="red")
louend.create_polygon(0, 0, 250, 150, 0, 300,fill="blue")

aken.mainloop()