from tkinter import  *

aken = Tk()
aken.resizable(0, 0)
aken.title("kalku")
aken.geometry("400x400")
aken.iconbitmap('xdkappa.ico')

tekst = Label(aken,
              text="Hind Käibemaksuta",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=1, column=0,sticky="w")

tekst = Label(aken,
              text="Käibemaksumär",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=2, column=0,sticky="w")

joon = Label(aken,
              text="-----------------------------------------",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=7, column=0,sticky="w")

tekst = Label(aken,
              text="Käibemaks",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=4, column=0,sticky="w")


var = IntVar()
valikukast = Radiobutton(aken,text="Valik 1", variable=var, value=1, command=naita_valikut)
valikukast.grid(row=1, column=0, sticky="w")
valikukast = Radiobutton(aken,text="Valik 2", variable=var, value=2, command=naita_valikut)
valikukast.grid(row=2, column=0,sticky="w")