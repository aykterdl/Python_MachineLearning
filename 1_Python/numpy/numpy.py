# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:26:56 2020

@author: Aykut
"""

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])

a = array.reshape(2,5)

print("shape: ", a.shape)
print("dimension: ", a.ndim)
print("data type: ", a.dtype.name)
print("size: ", a.size)
print("type: ", type(a))


print(np.zeros((3,4)))  #3x4 bouytlu 0 matrisi
print(np.ones((5,5)))   #5x5 boyutlu 1 matrisi
print(np.empty((3,3)))  #3x3 boyutlu matris

print(np.arange(10,50,5))   #10dan 50ye 5er 5er artıran matris
print((np.linspace(10,50,20)))  #10dan 50ye 0.20 artıran matris

# %% basic operation

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2) #a matrisinin karesi

print(np.sin(a)) #a matrisnin sinüsü

print(a<2)

print(a.dot(b.T))

#%% indexşng and slicing

import numpy as np
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[0])

print(array[0:4])

reverse_array = array[::-1] #indexler ters çevrilir
print(reverse_array)


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1])  # 1.sütunu al


print(array1[1,1:4])    # 1.satırda, 1.sütundan başla 4e kadar al


print(array1[-1,:]) # son satır
print(array1[:,-1]) # son sütun

# %%
# shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten
a = array.ravel() # array düz hale geldi, vektör.

array2 = a.reshape(3,3) # array tekrar 3x3 hale geldi.

arrayT = array2.T   

print(array2)
print(arrayT)

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[5,6]])


#array5 = np.column_stack((array1,array1))


# %% stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))

# horizontal
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))

print(array1)
print(array2)
print(array3)
print(array4)

#%% convert and copy

liste = [1,2,3,4]   # list

array = np.array(liste) #np.array

liste2 = list(array)

a = np.array([1,2,3])

b = a
b[0] = 5
c = a

d =  np.array([1,2,3])

e = d.copy()


print(array)
print(liste2)
print(a)
print(c)
print(d)
print(e)
