# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:07:40 2020

@author: Aykut
"""

import cv2
import numpy as np
import os,json

tani = cv2.face.LBPHFaceRecognizer_create()
tani.read('trainer.yml')
cascadePath = "data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font=cv2.FONT_HERSHEY_SIMPLEX
id = 0

dictionary={}
names = []
file = open("indexes.json","r")
dictionary = json.load(file)
cam = cv2.VideoCapture(0)

for key,value in dictionary.items():
    names.append(key)
    
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        id, oran = tani.predict(gray[y:y+h, x:x+w])
        print(id)
        
        if (oran < 70):
            id = names[id]
        else:
            id = "Tanınmayan Kişi"
        
        cv2.putText(frame, str(id), (x+5,  y-5), font, 1, (255,255,255),2)
        
        cv2.imshow('Uygulama', frame)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    
cam.release()
cv2.destroyAllWindows()
         