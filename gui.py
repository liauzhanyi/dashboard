from tkinter import *
import tkcalendar

root = Tk()
root.geometry("1000x1000")
root.title("Interactive Dashboard")

## Create Label Widget
## grid row and column is relative not absolute
label1 = Label(root, text = "TELEOS-2").grid(row=0, column=1)
label2 = Label(root, text = "Satellite:").grid(row=0, column=0) 

## Shove it to screen
# myLabel.pack() 

root.mainloop()