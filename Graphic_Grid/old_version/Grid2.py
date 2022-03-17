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
                self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1)

    def test(self):
        print(self.dessin)

    def color_list(self, color_list):
        self.color_list = color_list
        self.color_array = []
        for i in self.color_list:
            self.color_array.append(i)
        print(self.color_array)

    def grid_list(self, grid_list):
        #fill=self.color_array[i][j]
        self.grid_list = grid_list
        self.grid_height = len(self.grid_list)
        self.grid_width = len(self.grid_list[0])
        for i in range (self.grid_height):
            for j in range (self.grid_width):
                self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1,fill=self.color_array[self.grid_list[i][j]])

            

#dessin.bind("<Button-1>", select)
#dessin.bind("<Button1-ButtonRelease>", deselect)
#dessin.bind("<Button1-Motion>", move)




#fenetre.test()


