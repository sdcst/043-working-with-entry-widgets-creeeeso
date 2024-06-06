"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
import playsound as p

def name(e):
    data1 = e1.get()
    data2 = e2.get()
    data3 = e3.get()
    data = "Name: " + data1 +"\n " + "Student Number: " + data2 + "\n" + "Grade: " + data3

    l1.config(text=data)
    e2.delete(0,tk.END)
    e2.insert(0,data)
    e3.delete(0,tk.END)
    e3.insert(0,data)

win = tk.Tk()

b1 = tk.Button(win, text="Click to change the text")
l1 = tk.Label(win, text="Enter your student number:")
e1 = tk.Entry(win, width=15)
l2 = tk.Label(win, text="Enter your student number: ")
e2 = tk.Entry(win, width=15)
l3 = tk.Label(win, text="Enter your grade: ")
e3 = tk.Entry(win, width=15)

l1.grid(row=1, column=1)
e1.grid(row=2, column=1)


win.mainloop()