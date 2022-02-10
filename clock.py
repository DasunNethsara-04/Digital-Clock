#imports
from tkinter import *
import datetime

#main ui
root = Tk()
root.title('Digital Clock')
root.resizable(0, 0)

# function to get the current time
def getTime():
    time = datetime.datetime.now().strftime('%I:%M:%S %p')
    time_lbl.config(text=time)
    time_lbl.after(1000, getTime)


# create the label to display the current time
time_lbl = Label(root, font=('DS-Digital', 85), fg='red', bg='black')
time_lbl.pack()

# calling the getTime() function
getTime()

root.mainloop()
