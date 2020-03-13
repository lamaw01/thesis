import os,cv2;
import numpy as np
from PIL import Image;
import tkinter as tk
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.withdraw()

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
assure_path_exists("trainer/")

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    
    return faceSamples,Ids

faces,Ids = getImagesAndLabels('dataset')

id_count = 0
path = 'dataset'
    
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
for imagePath in imagePaths:
    Id=int(os.path.split(imagePath)[-1].split(".")[1])
    id_count= Id
        
if(id_count == 0):
    tkMessageBox.showerror("Error", "Dataset is Empty!")
else:
    s = recognizer.train(faces, np.array(Ids))
    recognizer.write('trainer/trainer.yml')
    tkMessageBox.showinfo("Info","Dataset Trained!")


