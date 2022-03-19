from tkinter import *

class Window:
    def __init__(self, titre, height, width):
        self.window = Tk()
        self.title = titre
        self.height = height
        self.width = width
        self.window.title(self.title)
        self.borderwidth = 10
        self.dessin=Canvas(self.window,height=self.height+1,width=self.width+1,borderwidth = self.borderwidth,highlightthickness=0) #height & width +1 for extern border
        self.dessin.pack()
        self.self_grid_list =[]
        return

    def define_grid(self, tile_height, tile_width):
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.tile_size_height = self.height / self.tile_height
        self.tile_size_width = self.width / self.tile_width
        
        for i in range (self.tile_height):
            for j in range (self.tile_width):
                self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1)
        return
    
    def color_list(self, color_list):
        self.color_list = color_list
        self.color_array = []
        for i in self.color_list:
            self.color_array.append(i)
        return

    def define_list(self, grid_list):
        self.grid_list = grid_list
        self.grid_height = len(self.grid_list)
        if self.grid_height > self.tile_height :
            print(f"Warning! There is too many lines({self.tile_height}), list({self.grid_height}) too long.")            
        elif self.grid_height < self.tile_height :
            print(f"Warning! There is not enough lines({self.tile_height}), list({self.grid_height}) too short.")

        self.grid_width = len(self.grid_list[0])
        if self.grid_width > self.tile_width :
            print(f"Warning! There is too many column({self.tile_width}), list({self.grid_width}) too long.")
        elif self.grid_width < self.tile_width :
            print(f"Warning! There is not enough column({self.tile_width}), list({self.grid_width}) too short.")
        
        for i in range (self.grid_height):
            l = []
            for j in range (self.grid_width):
                self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1,fill=self.color_array[self.grid_list[i][j]])
                l.append(self.grid_list[i][j])
            self.self_grid_list.append(l)
        self.dessin.update()
        return
    
    def update_list(self, grid_list):
        self.grid_list = grid_list
        for i in range (self.tile_height):
            for j in range (self.tile_width):
                if self.self_grid_list[i][j]!=self.grid_list[i][j]:
                    self.self_grid_list[i][j]=self.grid_list[i][j]
                    self.carreau=self.dessin.create_rectangle(j*self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.borderwidth, j*self.tile_size_width+self.tile_size_width+self.borderwidth, i*self.tile_size_height+self.tile_size_height+self.borderwidth,width=1,fill=self.color_array[self.grid_list[i][j]])
        self.dessin.update()
        return

    def onclick(self, click, function):
        if click == "left" or click == "l":
            self.dessin.bind("<Button-1>", function)
        elif click == "right" or click == "r":
            self.dessin.bind("<Button-3>", function)
        else:
            self.dessin.bind(click, function)#to add more event http://tkinter.fdex.eu/doc/event.html
            
    def tile_size(self):
        return self.tile_size_height,self.tile_size_width

    def tile_clicked(self,x,y):
        cx = x//self.tile_size_width
        cy = y//self.tile_size_height
        return int(cx),int(cy)

    def help(self):
        print("This program allows to have a graphic interface from a double list.\n")
        print("Constructor / init      :   my_window = Window('window name', height, width) --> my_window = Window('Grid',500,500) #500 px")
        print("Grid constructor        :   my_window.define_grid(number_of_horizontal_tiles,number_of_vertical_tiles --> my_window.define_grid(5,4) #int")
        print("List constructor        :   my_window.define_list(my_list) --> my_list=[[0,0,2,3],[1,6,4,3],[0,5,3,4],[3,4,2,1],[0,3,5,3]")
        print("Update list constructor :   my_window.update_list(my_list) --> update your list when you change it --> my_list[1,4]=2")
        print("Color constructor       :   my_window.color_list(my_colors) --> my_colors=['#F0F0F0','red','blue',...,'green']")
        print("Onclick constructor     :   my_window.onclick(left_or_right_click, function) --> my_window.onclick('left', selection)")
        print("Tile size               :   my_window.tile_size() --> get size of tiles in px return (heigh,width) #float --> (100.0, 125.0)")
        print("Tile clicked            :   my_window.tile_clicked(x,y) --> get number of the tile (x_position,y_position) #int --> (0, 4)")
        print("Created by Maxence Jamme 2022 \xa9")
