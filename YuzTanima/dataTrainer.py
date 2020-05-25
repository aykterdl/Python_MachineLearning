# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:58:34 2020

@author: Aykut
"""


import cv2
import numpy as np
from PIL import Image
import os,json

yol = 'dataset'
tani = cv2.face.LBPHFaceRecognizer_create()
tespit_et = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

def getResim(yol):
    yuzOrnekleri=[]
    indexes=[]
    labels=[]
    klasorler = os.listdir(yol)
    dictionary = {}
    
    for i,kl in enumerate(klasorler):
        dictionary[kl] = int(i)
        
    f = open("indexes.json","w")
    a = json.dump(dictionary,f)
    f.close()
 
    for kl in klasorler:
        for res in os.listdir(os.path.join(yol,kl)):
            PIL_img = Image.open(os.path.join(yol,kl,res)).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            id = int(dictionary[kl])
            yuzler = tespit_et.detectMultiScale(img_numpy)
            for (x,y,w,h) in yuzler:
                yuzOrnekleri.append(img_numpy[y:y + h, x:x + w])
                indexes.append(id)
    return yuzOrnekleri, indexes


yuzOrnekleri,indexes = getResim(yol)

tani.train(yuzOrnekleri, np.array(indexes))
tani.write('trainer.yml')