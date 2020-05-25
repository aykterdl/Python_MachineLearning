# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:21:25 2020

@author: Aykut
"""


import cv2
import os

cam = cv2.VideoCapture(0)
yuz_tespit = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

global user
user = input("Dataset eğitimi için isminizi giriniz: ")
print("\n Kameraya düzgün bir açıyla bakarak bekleyiniz...")
sayac = 0

os.mkdir('dataset/'+user)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = yuz_tespit.detectMultiScale(gray,1.5,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        sayac += 1
        path = "dataset/"+user + "/"
        cv2.imwrite(path+str(sayac)+".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('DATA', frame)
    k = cv2.waitKey(100) & 0xff
    
    if k == 27:
        break
    elif sayac >= 50:
        break

cam.release()
cv2.destroyAllWindows()