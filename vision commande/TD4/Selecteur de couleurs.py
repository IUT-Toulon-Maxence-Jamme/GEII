import cv2
import numpy as np
from sys import exit

import tkinter as tk
from tkinter import *
import pyperclip #pip install pyperclip

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'
def onclickbt():
    text = "("+str(Selector.b_min.get())+","+str(Selector.g_min.get())+","+str(Selector.r_min.get())+"),("+str(Selector.b_max.get())+","+str(Selector.g_max.get())+","+str(Selector.r_max.get())+")"
    #print(text)
    pyperclip.copy(text)

def bt_min():
    Selector.r_min.set(0)
    Selector.g_min.set(0)
    Selector.b_min.set(0)

def bt_max():
    Selector.r_max.set(255)
    Selector.g_max.set(255)
    Selector.b_max.set(255)

    
class RGB_selector(tk.Frame):
    def __init__(self, page, titre):
        self.page=page
        self.titre=titre
        self.page.title(self.titre)
        self.page.geometry("510x350")   #RGB scale
        self.r=Label(page,text="Couleur Rouge",fg="red")
        self.r.grid(row=0,column=0) 
        self.r_min = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.r_min.grid(row=0,column=1)
        self.r_max = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.r_max.grid(row=0,column=2)
        self.r=Label(page,text="Couleur Vert",fg="green")
        self.r.grid(row=1,column=0) 
        self.g_min = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.g_min.grid(row=1,column=1)
        self.g_max = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.g_max.grid(row=1,column=2)
        self.r=Label(page,text="Couleur Bleu",fg="blue")
        self.r.grid(row=2,column=0) 
        self.b_min = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.b_min.grid(row=2,column=1)
        self.b_max = Scale(page, from_=0, to=255, orient=HORIZONTAL, length=200)
        self.b_max.grid(row=2,column=2) #RGB view
        bouton=Button(page,text="Copy",font="arial 20 bold",bg='black',fg='white',command=onclickbt)
        bouton.grid(row=3,column=0)
        self.button_min=Button(page, text="",width=20,height=10,command=bt_min)
        self.button_min.grid(row=3,column=1,pady=20)
        self.button_max=Button(page, text="",width=20,height=10,command=bt_max)
        self.button_max.grid(row=3,column=2,pady=20)

def getcontour(img):
    #remove background
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY_INV)[1]
    #get max areas with convexe hull
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    hull = []
    areas=[cv2.contourArea(c) for c in contours]

    hull.append(cv2.convexHull(contours[np.argmax(areas)], False))

    #clone on image  
    filter_mask = np.zeros_like(img)
    cv2.drawContours(filter_mask, [hull[-1]], -1, (255,255,255), cv2.FILLED, 1)
    cv2.drawContours(filter_mask, hull, 0, 0, 5, 8)
    #copy and paste with the good image
    filtered=img.copy()
    filtered[filter_mask == 0] = 0
    return filtered


root_selector=Tk()
Selector = RGB_selector(root_selector,"Color selector")
bt_max()

img_name = 'rubikscube.jpg'
img = cv2.imread(img_name)
#cube = img#getcontour(img)
cube = getcontour(img)

if cube is None:
    print("le fichier cube n'existe pas / le chemin indiqué est mauvais")
    exit()   

blurred = cv2.GaussianBlur(cube,(5,5),0)
hsv = cv2.cvtColor(blurred,cv2.COLOR_RGB2HSV)
    
while True:
    #Get RGB scaler
    b_m,g_m,r_m=Selector.b_min.get(),Selector.g_min.get(),Selector.r_min.get()
    b_p,g_p,r_p=Selector.b_max.get(),Selector.g_max.get(),Selector.r_max.get()
    blue_m=(b_m,g_m,r_m)
    blue_p=(b_p,g_p,r_p)

    #Mask Generation
    mask = cv2.inRange(hsv,blue_m,blue_p)
    mask = cv2.erode(mask,None,iterations=1)
    mask = cv2.dilate(mask, None, iterations=1)
    #cv2.imshow("Frame",mask)
    nouvelle_image = np.zeros(img.shape,dtype=np.uint8)
    for i in range(3):   
        nouvelle_image[:,:,i] = img[:,:,i] * (mask[:,:]//255)
    cv2.imshow("nouvelle_image",nouvelle_image)
    
    #RGB view
    Selector.page.update()
    Selector.button_min.config(bg=_from_rgb((Selector.r_min.get(),Selector.g_min.get(),Selector.b_min.get())))
    Selector.button_max.config(bg=_from_rgb((Selector.r_max.get(),Selector.g_max.get(),Selector.b_max.get())))
    
    key = cv2.waitKey(50)
    # Press echap to end
    if key == 27:
      break
    



cv2.destroyAllWindows()
