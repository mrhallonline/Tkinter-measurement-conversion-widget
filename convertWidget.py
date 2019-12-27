from tkinter import *

window = Tk()

def convert_measurement():
    convert_grams = float(input_kg.get())*1000
    convert_pounds = float(input_kg.get())*2.20462
    convert_ounces = float(input_kg.get())*35.274
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    t1.insert(END, convert_grams)
    t2.insert(END, convert_pounds)
    t3.insert(END, convert_ounces)

b1=Button(window, text="convert", command=convert_measurement)
b1.grid(row=0, column=2)

e1=Label(window, text="Kg")
e1.grid(row=0, column=0)

input_kg=StringVar()
e2=Entry(window, textvariable=input_kg)
e2.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()