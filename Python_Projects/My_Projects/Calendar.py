from tkinter import *
import calendar

root = Tk()

root.title("My Own GUI Calendar")

year = 2021

myCal = calendar.calendar(year)
cal_year = Label(root, text=myCal, font="Arial 10")
cal_year.pack()

root.mainloop()
