from dbcon import *
import numpy as np
import cv2
import csv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face_LBPHFaceRecognizer.create();
rec.read("trainingdata.yml")
people=list()
id=0
font = cv2.FONT_HERSHEY_SIMPLEX
def liveVideo():
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            #print(id)
            conn=connector()
            id=con("SELECT username FROM studentinfp WHERE id=%s" %id)
            conn.__dis__()
            if id is None:
                id="Unknown"
            cv2.putText(img,str(id),(x,y+h),font,2.0,(0,0, 255))
            if(id not in set(people)):
                attandace(id)
            people.append(id)
        cv2.imshow('img',img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
#liveVideo()