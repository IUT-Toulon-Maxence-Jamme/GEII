# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:52:23 2022

@author: Moi
"""
#import des librairies
import cv2
from sys import exit
import numpy as np
#importing matplotlib
#import matplotlib.pyplot as plt 

#-----------CAHIER DE TEXTE-----------

img_name = 'paperwithmessage.ppm'

img = cv2.imread(img_name,0)

eq_img = cv2.equalizeHist(img)
cv2.imshow('Equalized Image',eq_img)

#-------------BRUCE BANNER-------------

img_name = 'bruce_banner.png'
img = cv2.imread(img_name)

h,w,t = img.shape
newimage = np.zeros((h,w,t),np.uint8) # dtype = np.uint8
newimage[:,:,:] = img[:,:,:] << 5;

#i,j = 0,0
#for k in range (t):
#    for i in range(h):
#        for j in range(w):
#            newimage[i][j][k] = img[i][j][k] << 5;
#            j += 1
#        i += 1
#    k += 1


affichage = np.concatenate((img,newimage), axis=1)
cv2.imshow('Bruce banner & Hulk',affichage)


#fin de programme
cv2.waitKey(0)
cv2.destroyAllWindows()
