from tkinter import *
import tkcalendar

root = Tk()
root.geometry("1000x1000")
root.title("Interactive Dashboard")

## Create Label Widget
myLabel = Label(root, text = "TELEOS-2")
myLabel.pack() # Shove it to screen

root.mainloop()