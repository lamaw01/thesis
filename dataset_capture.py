# Import OpenCV2 for image processing
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

# Start capturing video 
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0

assure_path_exists("dataset/")

path = 'dataset'

#counts the existing ids in dataset folder
id_count = 1
        
#get the path of all the files in the folder
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
#now looping through all the image paths and loading the Ids and the images
for imagePath in imagePaths:
#getting the Id from the image
    Id=int(os.path.split(imagePath)[-1].split(".")[1])
    if Id is None:
        id_count = 1
    else:
        id_count = Id+1
        
print(id_count)


# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.1, 4)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,255,255), 2)
        
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/face" + '.' + str(id_count) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

    # If image taken reach 30, stop taking video
    elif count>=30:
        tkMessageBox.showinfo("Info","Dataset Captured!")
        #print("Successfully Captured")
        break;

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()


