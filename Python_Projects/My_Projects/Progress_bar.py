import time
from tkinter import *
from tkinter.ttk import *

root = Tk()

progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress.place(x=100, y=100)

def loading():
    val = 0 
    while val < 109:
        progress['value'] = val
        root.update_idletasks()
        time.sleep(0.5)
        label = Label(root, text=str(val))
        label.place(x=280, y=200)
        val += 12
        if val == 108:
            val = 100
            break

button = Button(root, text="LOADING...", command=loading)
button.place(x=250, y=300)

root.mainloop()
