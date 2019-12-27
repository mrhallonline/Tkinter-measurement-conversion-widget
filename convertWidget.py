from tkinter import *

window = Tk()

b1=Button(window, text="convert")
b1.grid(row=0, column=1)

e1=Entry(window)
e1.grid(row=0, column=0, text="Kg")

t1=Text(window, height=10, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=10, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=10, width=20)
t3.grid(row=1, column=2)


window.mainloop()