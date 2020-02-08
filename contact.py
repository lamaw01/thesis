from tkinter import *
import os
import tkinter as tk

expression = "+63" 
  
def press(num): 
    global expression
  
    expression = expression + str(num) 
  
    equation.set(expression) 

def append():
    contact = expression_field.get()
    
    f = open("contact.txt","w+") 
    f.write(contact) 
    f.close()
    
    label1 = tk.Label(root, text = contact)
    canvas1.create_window(125, 60, window=label1)
    
def cancel():
    root.destroy()

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Contact")
    
    root.configure(background="white")
    
    canvas1 = tk.Canvas(root, width = 250, height = 375)
    canvas1.pack()
  
    equation = StringVar() 
    
    label1 = tk.Label(root, text='Input your number (+63)')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(125, 30, window=label1)
     
    expression_field = tk.Entry (root, textvariable=equation)
    expression_field.insert(0, "+63")
    canvas1.create_window(125, 100, window=expression_field)
  
#     equation.set('+63') 

    button1 = tk.Button(text='Ok', command=append)
    button2 = tk.Button(text='Quit', command=cancel)
    canvas1.create_window(85, 140, window=button1)
    canvas1.create_window(165, 140, window=button2)

    text1 = tk.Button(root, text='1', command=lambda: press(1))
    canvas1.create_window(75, 200, window=text1)

    text2 = tk.Button(root, text='2', command=lambda: press(2))
    canvas1.create_window(125, 200, window=text2)

    text3 = tk.Button(root, text='3', command=lambda: press(3))
    canvas1.create_window(175, 200, window=text3)

    text4 = tk.Button(root, text='4', command=lambda: press(4))
    canvas1.create_window(75, 240, window=text4)

    text5 = tk.Button(root, text='5', command=lambda: press(5))
    canvas1.create_window(125, 240, window=text5)

    text6 = tk.Button(root, text='6', command=lambda: press(6))
    canvas1.create_window(175, 240, window=text6)

    text7 = tk.Button(root, text='7', command=lambda: press(7))
    canvas1.create_window(75, 280, window=text7)

    text8 = tk.Button(root, text='8', command=lambda: press(8))
    canvas1.create_window(125, 280, window=text8)

    text9 = tk.Button(root, text='9', command=lambda: press(9))
    canvas1.create_window(175, 280, window=text9)

    textplus = tk.Button(root, text='+', command=lambda: press("+"))
    canvas1.create_window(75, 320, window=textplus)

    text0 = tk.Button(root, text='0', command=lambda: press(0))
    canvas1.create_window(125, 320, window=text0)

    textc = tk.Button(root, text='c', command=clear)
    canvas1.create_window(175, 320, window=textc)
  
    # start the GUI 
    root.mainloop() 
