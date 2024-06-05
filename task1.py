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
win = tk.Tk()

def name(e):
    print("Enter your name: ")
    print(f"Your name is{e}")
    data = e1.get()
    l1.config(text=data)
    e2.delete(0,tk.END)
    e2.insert(0,data)

l1 = tk.Label(win, text="N/A")
e1 = tk.Entry(win, width=15)
l2 = tk.Label(win, text="Enter your student number: ")
e2 = tk.Entry(win, width=15)
l3 = tk.Label(win, text="Enter your grade: ")
e3 = tk.Entry(win, width=15)

e1.pack()