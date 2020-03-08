#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()
root.resizable(False, False)

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("python start.py")
    
def function2():
    
    os.system("python dataset_capture.py")

def function3():

    os.system("python train_dataset.py")
    
def function4():
    
    os.system("python contact.py")
    
def function5():
    
    os.system("python reset_data.py")

def function6():

    root.destroy()

#setting title for the window
root.title("FBS'NT")

#creating a text label
Label(root, text="Child Safeness System",font=("roboto",20),fg="white",bg="#0D47A1",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Start",font=("roboto",20),bg="orange",fg='white',command=function1, relief=FLAT).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Capture Face",font=("roboto",20),bg="orange",fg='white',command=function2, relief=FLAT).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Train Face",font=('roboto',20),bg="orange",fg="white",command=function3, relief=FLAT).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Contact",font=('roboto',20),bg="orange",fg="white",command=function4, relief=FLAT).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Reset Data",font=('roboto',20),bg="orange",fg="white",command=function5, relief=FLAT).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('roboto',20),bg="#0D47A1",fg="white",command=function6, relief=FLAT).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
