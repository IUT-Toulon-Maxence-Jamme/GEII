# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:22:49 2022

@author: Moi
"""
#import des librairies
import cv2
from sys import exit
import numpy as np
#importing matplotlib

#initialisation des images
img_name_1 = 'Fabio.pgm'
img_name_2 = 'Lena.png'
img_name_3 = 'Baboon.png'
#lecture des images
img_1 = cv2.imread(img_name_1)
img_2 = cv2.imread(img_name_2) #img_2 = cv2.imread(img_name_2,0) N&B
img_3 = cv2.imread(img_name_3)
#verification de l'existance des images
if img_1 is None :
    print('"' + img_name_1 + '" ? Who is it?')
    exit()
if img_2 is None :
    print('"' + img_name_2 + '" ? Who is it?')
    exit()
if img_3 is None :
    print('"' + img_name_3 + '" ? Who is it?')
    exit()
#concatenation ( affichage sur la meme fenetre)
IMGs = np.concatenate((img_2,img_3), axis=1)
cv2.imshow("IMGs",IMGs)
#shape
(H,L,T) = img_2.shape
print("Hauteur", H, "Longeur", L, "Tableau", T)
#pixel min & max => couleur sur N&B
img_2_min = np.amin(img_1)
img_2_max = np.amax(img_1)
print("min = ", img_2_min, "max = ", img_2_max)
#BGR to GRAY
img_2_gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_2_gray",img_2_gray)
#BGR to YCRCB
img_2_YCC = cv2.cvtColor(img_2, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("img_2_YCC",img_2_YCC)


#---------Histogram---------

#Compute and plot the histogram of lena.pgm.
img_lena_pgm = cv2.imread(img_name_2,0)
#cv2.imshow('Classic Image',img_lena_pgm)
#plt.hist(img_lena_pgm.ravel()); plt.show()

#Normalize the histogram and plot, side by side, the original and normalized images.
img_lena_pgm = cv2.imread(img_name_2,0)

hist1 = cv2.calcHist([img_lena_pgm],[0],None,[256], [0,256])
#plt.plot(np.cumsum(hist1/(512*512)))


norm_img = np.zeros((512,512))
final_img = cv2.normalize(img_lena_pgm, norm_img, 0, 255, cv2.NORM_MINMAX)
#cv2.imshow('Normalized Image', final_img)

hist2 = cv2.calcHist([final_img],[0],None,[256], [0,256])
#plt.plot(np.cumsum(hist2/(512*512)))


eq_img = cv2.equalizeHist(img_lena_pgm)
#cv2.imshow('Equalized Image',eq_img)
hist3 = cv2.calcHist([eq_img],[0],None,[256], [0,256])
#plt.plot(np.cumsum(hist3/(512*512)))
#plt.title("Blue = Clissic / Orange = Normalized / Green = Equalized")

#plt.show()

#---------Quantication--------- 
img_lena_pgm = cv2.imread(img_name_2,0)
cv2.imshow('Classic Image',img_lena_pgm)
n = 6
new = np.zeros(img_lena_pgm.shape,dtype=np.uint8)
new[:,:] = 2**(n-1)+(img_lena_pgm[:,:]//(2**n))*(2**n)
cv2.imshow('02bits Image', new)








#fin de programme
cv2.waitKey(0)
cv2.destroyAllWindows()
