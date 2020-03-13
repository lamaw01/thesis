import os
import pathlib
import tkinter as tk
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.withdraw()

#change path if in raspi
#path = '/home/pi/Desktop/thesis/dataset'
#trainer_path = '/home/pi/Desktop/thesis/trainer'
path = 'dataset'
trainer_path = 'trainer'
trainer = 'trainer.yml'

imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
for imagePath in imagePaths:
    images = (os.path.split(imagePath)[-1])
    #delete file dataset
    try:
        if pathlib.Path(path+"/"+images).is_file():
            file_face = pathlib.Path(path+"/"+images)
            file_face.unlink()
    except FileNotFoundError:
        print("File not accessible")
    
#delete file trainer
try:
    if pathlib.Path(trainer_path+"/"+trainer).is_file():
        trainer_file = pathlib.Path(trainer_path+"/"+trainer)
        trainer_file.unlink()
        tkMessageBox.showinfo("Information","Dataset Deleted!")
    else:
        tkMessageBox.showerror("Error", "Dataset is Empty!")
except FileNotFoundError:
    print("File not accessible")


