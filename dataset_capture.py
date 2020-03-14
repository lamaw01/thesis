import cv2
import os
import tkinter as tk
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.withdraw()

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

assure_path_exists("dataset/")

cascade_name = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_name)

frameWidth= 640
frameHeight = 480
cam = cv2.VideoCapture(0)
cam.set(3, frameWidth)
cam.set(4, frameHeight)

count = 0
id_count = 1
        
path = 'dataset'
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

for imagePath in imagePaths:
    Id=int(os.path.split(imagePath)[-1].split(".")[1])
    if Id is None:
        id_count = 1
    else:
        id_count = Id+1
        
print(id_count)

while(True):
    success, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 5);
    for (x,y,w,h) in faces:   
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 1)
        count += 1
        cv2.imwrite("dataset/face" + '.' + str(id_count) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('frame', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;
    
    if cv2.getWindowProperty('frame', 4) < 1:
        break

    elif count>=50:
        tkMessageBox.showinfo("Info","Dataset Captured!")
        break;

cam.release()
cv2.destroyAllWindows()


