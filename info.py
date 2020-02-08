from tkinter import *
import os

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def defProceed():

    root.destroy()
    os.system("py firstpage.py")       

#setting title for the window
root.title("Info")

#creating a text label
Label(root, text="Reminder.. dont forget to not silent your phone",font=("times new roman",20),fg="white",bg="orange",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Proceed",font=("times new roman",20),bg="#0D47A1",fg='white',command=defProceed).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()

