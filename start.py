import os, cv2, numpy as np;
import sys
import pathlib
import tkinter as tk
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.withdraw()

cascade_name = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_name)

cameraNo = 0
frameWidth= 640
frameHeight = 480
cam = cv2.VideoCapture(cameraNo)
cam.set(3, frameWidth)
cam.set(4, frameHeight)

recognizer = cv2.face.LBPHFaceRecognizer_create();

try:
    if pathlib.Path('trainer/trainer.yml').is_file():
        recognizer.read('trainer/trainer.yml');
    else:
        tkMessageBox.showerror("Error", "Dataset is Empty!")
except FileNotFoundError:
    print("File not accessible")

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0;
id_count = []
counter = 0;

while True:
    if pathlib.Path('trainer/trainer.yml').is_file() is False:
        break;
    success, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 5);
    for (x,y,w,h) in faces:    
        roi_gray = gray[y:y + h, x:x + w]
        id,conf=recognizer.predict(roi_gray)
        if(conf < 70):
            #conf = "  {0}%".format(round(70 - conf))
            for i in range(id):
                if id not in id_count:
                    id_count.append(id)
            label = 'parent';
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2);
            cv2.putText(img,str(id)+" "+str(label)+" "+str(round(conf)),(x,y-10),font,0.55,(0,0,255),2)
            counter=0
        else:
            if len(id_count) == len(faces):
                id_count.clear()
                #conf = "  {0}%".format(round(130 - conf))
            if(len(id_count) >= 1):
                id = 'child';
                label = 'safe';
                detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255),2);
                cv2.putText(img,str(id)+" "+str(label)+" "+str(round(conf)),(x,y-10),font,0.55,(255,255,255),2)
            else:
                id = 'child';
                label = 'alone';
                detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1);
                cv2.putText(img,str(id)+" "+str(label)+" "+str(round(conf)),(x,y-10),font,0.55,(0,255,0),2)
                counter=counter+1

    print("id list "+str(id_count))
    print("found "+str(len(faces))+" face(s)")

    if(len(faces) == 0):
        counter = 0
        id_count.clear()

    if(counter < 0):
        counter = 0
            
    print("counter "+str(counter))

    if(counter == 20):
        os.system("python3 sms.py")
    elif(counter == 60):
        os.system("python3 dial.py")
        
    if(counter >= 90):
        counter = 0

    cv2.imshow('frame',img);

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty('frame', 0) < 0:
        break
  
cam.release();
cv2.destroyAllWindows();
