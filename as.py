from tkinter import *
from tkinter import messagebox


top = Tk()
top.geometry("200x100")
def start():
   messagebox.showinfo("Start")

B1 = Button(top, text = "Start", command = start)
B1.place(x = 10,y = 50)

def stop():
   messagebox.showinfo("Stop")

B2 = Button(top, text = "Stop", command = stop)
B2.place(x = 50,y = 50)



def Pause():
   messagebox.showinfo("Pause")

B3 = Button(top, text = "Pause", command = Pause)
B3.place(x = 90,y = 50)

top.mainloop()
