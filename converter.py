# importing tkinter
from tkinter import *
# importing os and changing working directory
# to the one the script is saved in
import os
os.chdir(os.path.dirname(__file__))

# start of window part
window = Tk()

# defining functions that will be called clicking buttons
def conversion():
    grams = float(e1_value.get()) * 1000
    t1.insert(END, grams)
    pounds = float(e1_value.get()) * 2.20462
    t2.insert(END, pounds)
    ounces = float(e1_value.get()) * 35.274
    t3.insert(END, ounces)

# message widgets
mkg = Message(window, text="Kg")
mkg.grid(row=0, column=1)
mfill = Message(window, text="^Fill this in^", width=100)
mfill.grid(row=1, column=0)
m1 = Message(window, text="Grams", width=50)
m1.grid(row=2, column=0)
m2 = Message(window, text="Pounds (lb)", width=50)
m2.grid(row=3, column=0)
m3 = Message(window, text="Ounces (oz)", width=50)
m3.grid(row=4, column=0)

# button widget
b1 = Button(window, text="Convert!", command=conversion) # no brackets, just referencing the function
b1.grid(row=1, column=1) # I can add ,rowspan=2 if button spans 2 rows

# entry widget
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=20)
e1.grid(row=0, column=0)

# text widgets
t1 = Text(window, height=1, width=10) # height and width are expressed in cells
t1.grid(row=2, column=1)
t2 = Text(window, height=1, width=10) # height and width are expressed in cells
t2.grid(row=3, column=1)
t3 = Text(window, height=1, width=10) # height and width are expressed in cells
t3.grid(row=4, column=1)

# end of window part
window.mainloop()