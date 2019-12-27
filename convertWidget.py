from tkinter import *

window = Tk()

def convert_measurement():
    convert_grams = float(input_kg.get())*1000
    convert_pounds = float(input_kg.get())*2.20462
    convert_ounces = float(input_kg.get())*35.274
    t1.insert(END, convert_grams)
    t2.insert(END, convert_pounds)
    t3.insert(END, convert_ounces)

b1=Button(window, text="convert from kg", command=convert_measurement)
b1.grid(row=0, column=1)

input_kg=StringVar()
e1=Entry(window, textvariable=input_kg)
e1.grid(row=0, column=0)

t1=Text(window, height=10, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=10, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=10, width=20)
t3.grid(row=1, column=2)

window.mainloop()