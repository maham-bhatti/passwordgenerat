from tkinter import *
import random
import string
from tkinter import ttk

def generate():
    password.set("".join(random.choices(data, k=int(b.get()))))

root = Tk()
root.title("Password Generator")
root.geometry('460x90')
root.config(bg="pink")
b = StringVar()
password = StringVar()
data = '!@#$%^&*()'+ string.digits + string.ascii_letters
ttk.Label(root, text = "length: ", ).grid(row = 0, column = 0, pady=10)
combo = ttk.Combobox(root, width = 13, textvariable = b)

combo["values"] = [i for i in range(8, 21)]
combo.grid(row =0, column = 1, pady = 10)
ttk.Button(root, text = "Generate the Password",command= generate).grid(row = 0, column= 0, padx = 5, pady=10)
ttk.Entry(root, textvariable= password, width = 27).grid(row=0, column=3, padx=10, pady=10)

root.mainloop()