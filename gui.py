from ssl import ALERT_DESCRIPTION_RECORD_OVERFLOW
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkcalendar
# from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x1000") ## window pop-up size
root.title("Interactive Dashboard")
# root.iconbitmap() ## i nsert logo

## Create LabelFrame: a bordered section. replace root with LabelFrame
frame = LabelFrame(root, padx=50, pady=50)
frame.grid(row=50, column=0)

def button1_click():
    # txt = Label(root, text="Done")
    # txt.grid(row=2, column=1)
    dm = dm_entry.get()
    Label(frame, text=f"Data Mnemonic Selected: {dm.upper()}").grid(row=3, column=0)
    return

def exitButton_click():
    root.quit()
    return

## Create Label Widget
## grid row and column is relative not absolute
## within Label():
##      - use image=ImageTk.PhotoImage(Image.open("path")) to insert image  
##      - bd for border
##      - relief (of border): FLAT, RAISED, SUNKEN, RIDGE, SOLID, GROOVE
label1 = Label(root, text="TELEOS-2").grid(row=0, column=1)
label2 = Label(root, text="Satellite:").grid(row=0, column=0) 
dm_label = Label(frame, text="Enter Data Mnemonic").grid(row=1, column=0)

## Create Button Widget
## within Button(),
##      - use padx, pady to change the size of button
##      - create a function that does something, 
##           use command = function to execute upon click 
##      - fg to change button text colour
##      - bg to change button background colour
##      - state=DISABLED to disabled button
button1 = Button(frame, text="Submit", command=button1_click, fg="blue")
button1.grid(row=2, column=0)
exitButton = Button(root, text="Exit", command=exitButton_click, fg="red")
exitButton.grid(row=999, column=0)

## Create entry box
## .get to retrieve text input
## .insert(0, "text") to insert default text in entry box
## .delete(0, END) to del all characters in entry
dm_entry = Entry(frame, width=20, borderwidth=3)
dm_entry.grid(row=1, column=1)

## Create Radiobutton
r = StringVar() ## or IntVar()
# r.set("0")

def radiobutton_clicked(val):
    rlabel = Label(root, text=val).grid(row=103, column=0)
    return

## can run this in a loop
Radiobutton(root, text="Option 1", variable=r, value='1', command=lambda: radiobutton_clicked(r.get())).grid(row=100, column=0)
Radiobutton(root, text="Option 2", variable=r, value='2', command=lambda: radiobutton_clicked(r.get())).grid(row=101, column=0)
Radiobutton(root, text="Option 3", variable=r, value='3', command=lambda: radiobutton_clicked(r.get())).grid(row=102, column=0)

## Create messagebox
def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    # assign to variable if using ask___ 
    messagebox.showwarning("CONFIDENTIAL", "EXIT NOW")
    return

msgButton = Button(root, text="pop up msg", command=popup)
msgButton.grid(row=4, column=0)

root.mainloop()
# root.quit() to exit

#####################
## Other Functions ##
#####################

## Create new window
Toplevel()

## Open file dialog box
from tkinter import filedialog
filedialog.askopenfilename()

## Slider
## can be used to resize window
Scale()

## Checkbox
Checkbutton()

## Drop down menu
OptionMenu()

## Building database
