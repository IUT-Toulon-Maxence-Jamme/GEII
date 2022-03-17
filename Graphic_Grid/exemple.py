from Grid_Creator import *
from random import *
import time

color=['#F0F0F0','red','blue','green','yellow','pink','purple','gray','orange']

fenetre = Window("Grille", 500, 500)
x, y = 4, 5
fenetre.define_grid(y,x)
fenetre.color_list(color)

#creation of list
liste=[]
for i in range(y):
    l=[]
    for j in range(x):
        l.append(randint(1,8))
    liste.append(l)
fenetre.define_list(liste)

def unselect(event):
    x1=event.x
    y1=event.y    
    (cx,cy) = fenetre.tile_clicked(x1,y1)
    liste[cy][cx] = 0
    fenetre.update_list(liste)
    return

def reselect(event):
    x1=event.x
    y1=event.y
    (cx,cy) = fenetre.tile_clicked(x1,y1)
    liste[cy][cx] = randint(1,8)
    fenetre.update_list(liste)
    return

def deletselect(event):
    for i in range(x*y):
        liste[i//x][i%x] = 0
        fenetre.update_list(liste)
        time.sleep(0.01)
        
fenetre.onclick("l", unselect)
fenetre.onclick("r", reselect)
fenetre.onclick("<Double-Button-1>", deletselect)





fenetre.help()




fenetre.window.mainloop()
