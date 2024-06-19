#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk

win = tk.Tk()

def clickFunction(e):
    data1 = e1.get()
    data2 = e2.get()
    number1 = float(data1)
    number2 = float(data2)
    data = ((number1**2) + (number2**2)) ** 0.5
    e3.insert(0,data)

b1 = tk.Button(win, text="Click to find the hypotenuse")
l10 = tk.Label(win, text="There are 3 side in a triangle, 2 short side (typically called side a and b)\nand one long side (the hypotenuse)")
l1 = tk.Label(win, text="Enter side a: ")
e1 = tk.Entry(win, width=15)
l2 = tk.Label(win, text="Enter side b:")
e2 = tk.Entry(win, width=15)
l3 = tk.Label(win, text="hypotenuse")
e3 = tk.Entry(win, width=15)

b1.bind("<Button-1>", clickFunction)

l1.grid(row=1, column=1)
e1.grid(row=1, column=2)
l2.grid(row=2, column=1)
e2.grid(row=2, column=2)
l3.grid(row=3, column=1)
b1.grid(row=4, column=2)
e3.grid(row=3, column=2)

win.mainloop()