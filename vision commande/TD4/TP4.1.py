import cv2
import numpy as np
liste = []

def mask_func(color,c_min,c_max,image):
    mask = cv2.inRange(hsv,c_min,c_max)
    mask = cv2.erode(mask,None,iterations=1)
    mask = cv2.Canny(mask, 50, 100)
    mask = cv2.dilate(mask, None, iterations=1)
    ret, thresh = cv2.threshold(mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow('thresh', mask)
    output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)
    mask = cv2.bitwise_not(mask)
    image = cv2.bitwise_and(img, image, mask = mask)
    for i in range(output[0]-1):
        cv2.putText(image, color, (int(output[3][i+1][0])-15,int(output[3][i+1][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        l = []
        l.append(int(output[3][i+1][0]))
        l.append(int(output[3][i+1][1]))
        liste.append(l)
    return image


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


img_name = 'R.jpg'
img = cv2.imread(img_name)
nouveau_cube = getcontour(img)

blurred = cv2.GaussianBlur(nouveau_cube,(11,11),0)
hsv = cv2.cvtColor(blurred,cv2.COLOR_RGB2HSV)

liste_couleur = [["Bleu",(164,0,0),(255,255,255)],["Vert",(44,0,0),(88,255,255)]]
for i in liste_couleur:
    img=mask_func(i[0],i[1],i[2],img)
cv2.imshow('Final', img)



#fin de programme
cv2.waitKey(0)
cv2.destroyAllWindows()
