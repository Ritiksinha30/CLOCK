from tkinter import Label , Tk
import time

root = Tk()
root.title("Digital Clock")
root.geometry("490x150")
root.resizable(1,1)

txt_font = ("Arial", 68 , "bold")
background = "Red"
foreground = "#363529"
border_width = 25

lbl = Label(root, font=txt_font, bg=background, fg=foreground,bd=border_width)
lbl.grid(row=0,column=1)

def digital_clock():
    time_live= time.strftime("%H: %M: %S")
    lbl.config(text=time_live)
    lbl.after(200, digital_clock)


digital_clock()

root.mainloop()