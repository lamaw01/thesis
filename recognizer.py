import os, cv2, numpy as np;
import sys
from playsound import playsound
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
filename='filename';
dict = {'item1': 1}
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0;
id_count = []
counter = 0;

while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, 1.1, 4);
    for (x,y,w,h) in faces:  
        roi_gray = gray[y:y + h, x:x + w]
        id,conf=recognizer.predict(roi_gray)
        if(conf <= 90):
            #for every id detected it adds to the id_count list
            for i in range(id):
                if id not in id_count:
                    id_count.append(id)
            id = id;
            #green color means known face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1);
            #id label color green
            cv2.putText(img,str(id)+" "+str(round(conf)),(x,y-10),font,0.55,(0,255,0),1)
        elif(conf > 90 and conf <= 120):
            id = 'approximately';
            #orange color means unknown face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,140,255),1);
            #id label color orange
            cv2.putText(img,str(id)+" "+str(round(conf)),(x,y-10),font,0.55,(0,140,255),1)
            id_count.clear()           
        else:  
            id = 'unknown';
            #red color means unknown face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1);
            #id label color red
            cv2.putText(img,str(id)+" "+str(round(conf)),(x,y-10),font,0.55,(0,0,255),1)
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

    #play the sound if counter reach 100
    if(counter >= 100):
        playsound('transactionSound.mp3')
        print("Transaction Blocked")
        break;

    #show the frame
    cv2.imshow('frame',img);

    #closes the program if presses q
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

#destroy window    
cap.release();
cv2.destroyAllWindows();
