import os, cv2, numpy as np;
#import time
import sys
from playsound import playsound
#start=time.time()
#period=8
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
flag = 0;
facename = '';
filename='filename';
dict = {'item1': 1}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0;
id_count = []

while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, 1.1, 4);
    for (x,y,w,h) in faces:  
        roi_gray = gray[y:y + h, x:x + w]
        id,conf=recognizer.predict(roi_gray)
        print(id_count)
        if(conf <= 80):
            for i in range(id):
                if id not in id_count:
                    id_count.append(id)
            id = id;
            #green color means known face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2);
            #id label color green
            cv2.putText(img,str(id)+" "+str(round(conf)),(x,y-10),font,0.55,(0,255,0),1)
        else:
            id = 'unknown';
            #red color means unknown face
            detected_face = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2);
            #id label color red
            cv2.putText(img,str(id)+" "+str(round(conf)),(x,y-10),font,0.55,(0,0,255),1)
        print("Found "+str(len(faces))+" face(s)")
        
##        else:
##            id = 'unknown';           
##            flag=flag+1
##            break
        
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame',img);
##    cv2.imshow('gray',gray);
##    if flag == 10:
##        playsound('transactionSound.mp3')
##        print("Transaction Blocked")
##        break;
##    if time.time()>start+period:
##        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;
    
##def getPath(path):
##    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
##    for imagePath in imagePaths:
##        print(os.path.split(imagePath)[1].split(".")[0])
##getPath('dataset')
##
##
##for str(len(faces)) in faces:
##+" "+str(conf)
cap.release();
cv2.destroyAllWindows();
