from tkinter import *

class Window:
    def __init__(self, titre, height, width):
        self.window = Tk()
        self.title = titre
        self.height = height
        self.width = width
        
        self.window.title(self.title)
        self.borderwidth = 10
        self.dessin=Canvas(self.window,height=self.height+1,width=self.width+1,borderwidth = self.borderwidth,highlightthickness=0)
        self.dessin.pack()

        

        
        
    def manual_grid(self, tile_height, tile_width, tile_size):
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.tile_size = tile_size
        for i in range (self.tile_height):
            for j in range (self.tile_width):
                self.carreau=self.dessin.create_rectangle(j*self.tile_size+self.borderwidth, i*self.tile_size+self.borderwidth, j*self.tile_size+self.tile_size+self.borderwidth, i*self.tile_size+self.tile_size+self.borderwidth)
        
        
    def auto_grid(self, tile_height, tile_width):
        #self.dessin.delete('ALL')
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.tile_size_height = self.height / self.tile_height
        self.tile_size_width = self.width / self.tile_width
        for i in range (self.tile_height):
            for j in range (self.tile_width):
                #(print(j*self.tile_size_width+self.marge,i*self.tile_size_height+self.marge,j*self.tile_size_width+self.tile_size_width,i*self.tile_size_height+self.tile_size_height)
                self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1)

    def test(self):
        #self.carreau.fill = 'blue'
        print(self.dessin)

#print('p1=',piece1)
#print('p2=',piece2)
#print('p3=',piece3)
#print('p4=',piece4)

#fen=Tk()
#fen.title("Grille")

#fend=Frame(fen, bd=4,bg='white',relief=RAISED)
#fend.grid(row=0,column=1)

#feng=Frame(fen,relief=RAISED)
#feng.grid(row=0,column=0)


#dessin=Canvas(fend,height=1000,width=900)
#dessin.pack()
#dessin.bind("<Button-1>", select)
#dessin.bind("<Button1-ButtonRelease>", deselect)
#dessin.bind("<Button1-Motion>", move)



fenetre = Window("Grille", 500, 500)

manual = 0
if manual == 1:
    fenetre.manual_grid(5, 3, 50)
else :
    fenetre.auto_grid(50,30)

#fenetre.test()


