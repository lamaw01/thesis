from tkinter import *
import os

root=Tk()
root.resizable(False, False)
root.configure(background="white")

def defProceed():
    root.destroy()
    os.system("python3 main_menu.py")       

root.title("Info")
Label(root, text="Reminder.. dont forget to not silent your phone",font=("roboto",20),fg="white",bg="orange",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Ok",font=("roboto",20),bg="#0D47A1",fg='white',command=defProceed, relief=FLAT).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()

