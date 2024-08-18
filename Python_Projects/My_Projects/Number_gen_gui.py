from tkinter import *
import random

root = Tk()
root.geometry("5000x500")
root.title("Number Generator")

def Ref():
    x = random.randint(0,10)
    randomRef = x
    randomRef = x * randomRef
    rand.set(randomRef)

Tops = Frame(root,height=50, relief=SUNKEN)
Tops.pack(side=TOP, fill=X)

labelinfo = Label(Tops, font=('arial', 30, 'bold'), text = "Number Generator", fg="black", bd=10, anchor="w")
labelinfo.grid(row=0, column=0)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

labelid = Label(f1, font=('arial', 30, "bold"), text="Number Gen", fg="brown", bd=20, anchor="w")
labelid.grid(row=0, column=0)

rand = StringVar()
textid=Entry(f1, font=("arial", 30, "bold"), textvariable=rand, bd=6, insertwidth=6, bg="yellow", justify="right")
textid.grid(row=0, column=1)

buttontotal = Button(f1, pady=0, bd=10, fg="black", font=("arial", 30, "bold"), width=10, text="Generate", bg="red", command=Ref)
buttontotal.grid(row=1, column=1)

root.mainloop()
