from tkinter import *
import os
from datetime import datetime;

root=Tk()
root.resizable(False, False)

root.configure(background="white")

def function1():
    os.system("python3 start.py")
    
def function2():
    os.system("python3 dataset_capture.py")

def function3():
    os.system("python3 train_dataset.py")
    
def function4():
    os.system("python3 contact.py")
    
def function5():
    os.system("python3 reset_data.py")

def function6():
    root.destroy()

root.title("FBS'NT")
Label(root, text="Child Safeness System",font=("roboto",20),fg="white",bg="#0D47A1",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Start",font=("roboto",20),bg="orange",fg='white',command=function1, relief=FLAT).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Capture Face",font=("roboto",20),bg="orange",fg='white',command=function2, relief=FLAT).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Train Face",font=('roboto',20),bg="orange",fg="white",command=function3, relief=FLAT).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Contact",font=('roboto',20),bg="orange",fg="white",command=function4, relief=FLAT).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Reset Data",font=('roboto',20),bg="orange",fg="white",command=function5, relief=FLAT).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Exit",font=('roboto',20),bg="#0D47A1",fg="white",command=function6, relief=FLAT).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
