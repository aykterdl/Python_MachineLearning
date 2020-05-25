# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:35:08 2020

@author: Aykut
"""

import cv2

class kamera:
    def __init__(self,ip):
        self.ip = ip
    
    def ac(self):
        video = cv2.VideoCapture(self.ip)
        while True:
            ret, frame = video.read()
            cv2.imshow('Uygulama',frame)
            cv2.waitKey(1)
            
    def kapat():
        cv2.destroyAllWindows()

cam1 = kamera(0)
cam1.ac()