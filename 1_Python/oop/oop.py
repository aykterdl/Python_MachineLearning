# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:08:14 2020

@author: Aykut
"""

class Otomobil:
    
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        
    def getOtoInfo(self):
        return self.marka + " / " + self.model + " / " + self.yil        
        
oto1 = Otomobil("Volkswagen","Golf","2019")
print(oto1.getOtoInfo())