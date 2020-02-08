#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("python dataset_capture.py")
    
def function2():
    
    os.system("python training_dataset.py")

def function3():

    os.system("python recognizer.py")
    
def function4():
    
    os.system("python reset_data.py")
    
def function5():
    
    os.system("python contact.py")

def function6():

    root.destroy()

#setting title for the window
root.title("FBSn't")

#creating a text label
Label(root, text="FACE RECOGNITION",font=("times new roman",20),fg="white",bg="orange",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Reset Dataset",font=('times new roman',20),bg="#0D47A1",fg="white",command=function4).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Contact",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="orange",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
