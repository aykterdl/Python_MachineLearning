# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:22:36 2019

@author: teknopar
"""
# %%
# variable

# 15.02.2019 python temelleri atiliyor.
# 3 cesit component
# 1_variable - herhangi bir tür olabilir.
# 2_function
# 3_object

var1 = 10 #integer
var2 = 15

gun = "Cuma" #string
var3 = 19.07 #double
# %% string

s = "Aykut Erdal"
variable_type = type(s)

print(s)

var1 = "Ankara"
var2 = "İstanbul"
var3 = var1 + var2
print(var3)

uzunluk = len(var3)
print(uzunluk)
print(var3[2])
# %% numbers
int_sayi = 37
float_sayi = 6.37

float(int_sayi)

# %% built in function

str1= "deneme"
flot1= 10.6

str2= "3706"
int(str2)
print(str2)

# %% user defined function

var1 = 10
var2 = 100

output = (((var1+var2)*50)/100)

def funcum(a,b):
    """
    deneme asdasdgasd
    3 tırnak arasına açıklama yazılıyor.
    
    """
    output = (((a+b)*50)/100)
    
    return output


print(funcum(var1,var2))
sonuc = funcum(152,658)
print(sonuc)

# %% default and flexible function

def cember_cevresi(r):
    """
    pi sayısı 3.14 alınacaktır.
    """
    cevre = (2 * 3.14 * r)
    return cevre
    
cevresi = cember_cevresi(6)
print(cevresi)

# flexible

def hesapla(boy, kilo, *args):
    output = (boy + kilo)*args[0]
    return output

#def hesapla(boy, kilo, yas):
#    output = (boy + kilo) * yas
#    return output

# %%  QUIZ
    
# Bölüm 2, Video 9

# %%