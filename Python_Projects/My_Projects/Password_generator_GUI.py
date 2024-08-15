from tkinter import *
from tkinter import ttk
import random
import string

def generate():
    password.set(''.join(random.choices(data, k = int(n.get()))))
    
window = Tk()
n = StringVar()
password = StringVar()
data = '!@#$%^&*()' + string.ascii_letters + string.digits

ttk.Label(window, text="Length: ", ).grid(column=0, row=0, pady=10)

combo=ttk.Combobox(window, width=4, textvariable = n)
combo['values'] = [i for i in range(6, 21)]
combo.grid(column=1, row=0, pady=10)

ttk.Button(window, text="generate", command=generate).grid(row=0, column=0, pady=10, padx=5)
ttk.Entry(window, textvariable=password).grid(row=0, column=3, padx=5, pady=10)

window.mainloop()

