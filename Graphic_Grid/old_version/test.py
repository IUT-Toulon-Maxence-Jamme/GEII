from Grid4 import *
from random import *
import time
fenetre = Window("Grille", 500, 500)

x = 5
y = 4

fenetre.define_grid(x,y)

color=['#F0F0F0','red','blue','green','yellow','pink','purple','gray','orange']
fenetre.color_list(color)

liste=[]
for i in range(x):
    l=[]
    for j in range(y):
        l.append(randint(1,7))
    liste.append(l)
fenetre.define_list(liste)

def test(event):
    x1=event.x
    y1=event.y    
    (cx,cy) = fenetre.tile_clicked(x1,y1)
    print(cx,cy)
    return

def tes(event):
    x1=event.x
    y1=event.y
    (cx,cy) = fenetre.tile_clicked(x1,y1)
    liste[cy][cx] = randint(1,8)
    fenetre.update_liste(liste)
    return
    
'''fenetre.grid_list(liste)
print(liste)
liste[0][0] = 4
#fenetre.test()((
print(liste)    
fenetre.test(liste)
print("modif")
liste[0][0] = 0
fenetre.test(liste)

print(test)'' '

fenetre.define_list(liste)
print(liste)
liste[0][0] = 4
fenetre.update_list(liste)
liste[1][1] = 4
#fenetre.onclick("left", test)
fenetre.onclick("r", tes)
fenetre.onclick("l", fenetre.onclick_list)
fenetre.update_list(liste)

time.sleep(1)

liste[0][0] = 1
fenetre.update(liste)
time.sleep(1)
liste[0][0] = 2
fenetre.update(liste)
' ''
fenetre.update(liste)
time.sleep(1)

liste[0][0] = 1
fenetre.update(liste)
print('avant')
time.sleep(3)
print("apres")
liste[0][0] = 3
fenetre.update(liste)
time.sleep(1)
'''

time.sleep(1)
for i in range(x*y):
    liste[i//y][i%y] = 0
    fenetre.update(liste)
    time.sleep(0.01)

fenetre.help()




fenetre.window.mainloop()
