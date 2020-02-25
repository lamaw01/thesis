import os, cv2, numpy as np;
import sys
import pathlib
import tkinter as tk
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.withdraw()

#harcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#use camera
cam = cv2.VideoCapture(0);
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#algorithm used
recognizer = cv2.face.LBPHFaceRecognizer_create();

#check if file exist
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
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)));
    for (x,y,w,h) in faces:    
        roi_gray = gray[y:y + h, x:x + w]
        id,conf=recognizer.predict(roi_gray)
        if(conf <= 70):
            conf = "  {0}%".format(round(70 - conf))
            #for every id detected it adds to the id_count list
            for i in range(id):
                if id not in id_count:
                    id_count.append(id)
            if len(id_count) == len(faces):
                #green color means known face
                detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1);
                #id label color green
                cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(0,255,0),1)
            else:
                label = 'safe';
                detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255),1);
                cv2.putText(img,str(id)+" "+str(label)+" "+str(conf),(x,y-10),font,0.55,(255,255,255),1)         
        else:
            conf = "  {0}%".format(round(130 - conf))
            id = 'unknown';
            #red color means unknown face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1);
            #id label color red
            cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(0,0,255),1)
            id_count.clear()

    print("id list "+str(id_count))
    print("found "+str(len(faces))+" face(s)")

    #clear the id_count
    if(len(id_count) > len(faces)):
            id_count.clear()

    if(len(faces) == 0):
            id_count.clear()
    
    #increments a counter to call the gsm if reached an specific amount
    if(len(id_count)) == (len(faces) or len(id_count) == 0):
        counter=counter+1
        
    else:
        if counter != 0:
            counter=counter-1
            
    print("counter "+str(counter))

    #play the sound if counter reach 20
    if(counter == 20):
        #call gsm sms scipt
        os.system("python3 sms.py")
        counter=counter+10
    elif(counter == 70):
        #call gsm dial scipt
        os.system("python3 dial.py")
        counter=counter+10
        
    if(counter >= 100):
        #reset id_counter
        counter = 0
    #show the frame
    cv2.imshow('frame',img);

    #closes the program if presses q
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

#destroy window    
cam.release();
cv2.destroyAllWindows();

