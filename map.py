"""map.py
    store all of the tiles and game objects and handle the movement
"""

from gameobject import GameObject;
from tile import Tile;
from bin import Bin;
from button import Button;
from fileio import FileIO;

from pygame import mouse;
from pygame import font;
import os;
import tkFileDialog;

class Map:
    """store all of the tiles and GameObjects as arrays and handle drawing and
    mouse movement."""


    def __init__(self):

        #bin for objects and tiles
        self._object_bin = Bin(0, 0, 150, 450);
        self._tile_bin = Bin(600, 225, 150, 225);

        #2d list of tiles that are on the map
        self._tiles = [];

        #list of GameObjects on the map
        self._objects = [];

        #offsets for the map having been dragged
        self._x_offset = 0;
        self._y_offset = 0;

        #currently selected Placeable item
        self._selected = None;

        #whether or not the map is scrolling currently
        self._scrolling = False;

        #list to store any buttons
        self._buttons = [];

        self.init_bins();

    @property
    def object_bin(self):
        '''handles the bin to hold all of the placeable GameObjects'''
        return self._object_bin;

    @property
    def tile_bin(self):
        '''handles the bin to store all of the tile templates'''
        return self._tile_bin;

    @property
    def objects(self):
        '''stores all objects currently placed on the map'''
        return self._objects;

    @property
    def tiles(self):
        '''store the state of each tile in this 2d world'''
        return self._tiles;

    @property
    def x_offset(self):
        '''offset by which all objects need to be drawn on the x-axis which is
        based and modified by the mouse movement.'''
        return self._x_offset;

    @x_offset.setter
    def x_offset(self, x_offset):
        self._x_offset = x_offset;

    @property
    def y_offset(self):
        '''the offset by which all items in the map need to be drawn for the
        y-axis and is modified by the mouse'''
        return self._y_offset;

    @y_offset.setter
    def y_offset(self):
        self._y_offset = self.y_offset;

    @property
    def selected(self):
        '''tracks the information for the currently being moved GameObject or
        Tile template'''
        return self._selected;

    @selected.setter
    def selected(self, selected):
        self._selected = selected;

    @property
    def scrolling(self):
        '''boolean flag storing whether or not the mouse wheel is currently
        pressed down therefor the map needs to scroll or pan'''
        return self._scrolling;

    @scrolling.setter
    def scrolling(self, scrolling):
        self._scrolling = scrolling;

    @property
    def buttons(self):
        '''store the buttons on the screen, load and save'''
        return self._buttons;

    def init_bins(self):
        '''initialize the bins their default state which involves identifying
        the images in the resources folder and applying them to the correct
        bin'''

        #get list of game_object files
        game_objects = os.listdir('resources/game_objects');
        for item in game_objects:
            self.object_bin.add_item(GameObject('resources/game_objects/{}'.format(item)));


        #get list of terrain files and add them to the texture bin
        tiles = os.listdir('resources/terrain');
        for item in tiles:
            self.tile_bin.add_item(Tile('resources/terrain/{}'.format(item)));

        for i in range(0, 450 / Tile.HEIGHT):
            self.tiles.append([]);
            for j in range(0, 450 / Tile.WIDTH):
                tile =Tile('resources/terrain/grass0.png',
                              x = (self.object_bin.rect.width + j* Tile.WIDTH),
                              y = i * Tile.HEIGHT);
                tile.in_bin = False;
                self.tiles[i].append(tile);

        self.buttons.append(Button('Save', 600, 25, self.save));
        self.buttons.append(Button('Load', 650, 25, self.load));

    def update(self):
        """move the objects or tiles as needed and handle the expansion of the
        tile 2d list as needed based on the user panning the map."""
        delta = mouse.get_rel();
        if(self.selected != None):
            self.selected.move(delta[0], delta[1]);

        if(self.scrolling):
            self.x_offset += delta[0];
            self.y_offset += delta[1];

            #if the tiles have gone to far to the left on the x append a column
            #~of tiles
            #Use the top right tile to get the x and y value
            #advance through the rows and add a column of tiles to the
            #~right
            top_left = self.tiles[0][0];
            bottom_right = self.tiles[
                                    len(self.tiles) - 1][len(self.tiles[0]) - 1];
            if(bottom_right.rect.right + self.x_offset < 650):
                for i, row in enumerate(self.tiles):
                    right = self.tiles[i][len(self.tiles[i]) - 1];
                    tile = Tile('resources/terrain/grass0.png',
                                x = right.rect.right,
                                y = right.rect.y);
                    tile.in_bin = False;
                    row.append(tile);

            #if the tiles have gone too far up on the y append a row to tiles
            #~and fill with Tiles
            if(bottom_right.rect.bottom + self.y_offset < 500):
                row = [];
                for i in range(0, len(self.tiles[0])):
                    bottom = self.tiles[len(self.tiles) - 1][i];
                    tile = Tile('resources/terrain/grass0.png',
                               x = bottom.rect.x,
                               y = bottom.rect.y + Tile.HEIGHT);
                    tile.in_bin = False;
                    row.append(tile);
                self.tiles.append(row);


            #if the tiles have gone too far right on the x advance throught the
            #~rows and insert a row of tiles on the left
            if(top_left.rect.x  + self.x_offset > 100):
                for i, row in enumerate(self.tiles):
                    left = self.tiles[i][0];
                    tile = Tile('resources/terrain/grass0.png',
                                x = left.rect.x - Tile.WIDTH,
                                y = left.rect.y);
                    tile.in_bin = False;
                    row.insert(0, tile);

            #if the tiles have gone too far down on the y insert a new row at
            #~the begining and fill it with tiles
            if(top_left.rect.y + self.y_offset > -50):
                row = [];
                for i in range(0, len(self.tiles[0])):
                    top = self.tiles[0][i]
                    tile = Tile('resources/terrain/grass0.png',
                                x = top.rect.x,
                                y = top.rect.y - Tile.HEIGHT);
                    tile.in_bin = False;
                    row.append(tile);
                self.tiles.insert(0, row);


    def draw(self, screen):
        """draw the objects and tiles to the screen"""
        for row in self.tiles:
            for col_item in row:
                col_item.draw(screen, self.x_offset, self.y_offset);

        for item in self.objects:
            item.draw(screen, self.x_offset, self.y_offset);

        self.object_bin.draw_items(screen, self.x_offset, self.y_offset);
        self.tile_bin.draw_items(screen, self.x_offset, self.y_offset);

        for item in self.buttons:
            item.draw(screen);

        if(self.selected != None):
            if(not self.selected.in_bin):
                x_offset = self.x_offset;
                y_offset = self.y_offset;
            else:
                x_offset = 0;
                y_offset = 0;
            self.selected.draw(screen, x_offset, y_offset);


    def save(self):
        '''identify the path which the user wishes to save the map to and pass
        the path and data along to the FileIO class'''
        file = tkFileDialog.asksaveasfilename();
        FileIO.save(file, (self.tiles, self.objects, self.x_offset,
                           self.y_offset));


    def load(self):
        '''identify the path by which too load the map info and pass along the
        data to the FileIO class and store the information to relavent
        attributes.'''
        file = tkFileDialog.askopenfilename();
        items = FileIO.load(file);
        self.tiles = items[0];
        self.objects = items[1];
        self.selected = None;
        self.x_offset = items[2];
        self.y_offset = items[3];


    def mouse_down(self, point, button):
        """go through the objects list and if the point is in the bounds of the
        object, set the objects moving property to True and add a duplicate of
        the object in the bin if it was in the bin

        go through the tile_bin list and if the point is in the bounds of the
        tile set it to moving and create a copy of it in the tile_bin

        if the mouse wheel is pressed down set the scrolling boolean flag

        if the mouse wheel is scrolled pass on the data to the relavent bins."""
        if(button == 1):
            #have an intermediatery variable to store the item before it goes to
            #~selected

            item = self.object_bin.mouse_down(point);

            #check if item is = None and if so check tile bin
            if(item == None):
                item = self.tile_bin.mouse_down(point);

            for button in self.buttons:
                if(button.rect.collidepoint(point)):
                    button.click();

            point = list(point);
            point[0] -= self.x_offset;
            point[1] -= self.y_offset;

            #check if item None and if so check the objects list
            if(item == None):
                for i in self.objects:
                    if(i.contains_point(point)):
                        item = i;
                        self.objects.remove(i);
            if(item is not None):
                self.selected = item;
        elif(button == 2):
            self.scrolling = True;
        elif(button == 4):
            if(self.object_bin.contains_point(point)):
                self.object_bin.scroll_up();
            elif(self.tile_bin.contains_point(point)):
                self.tile_bin.scroll_up();

    def mouse_up(self, point, button):
        """advance trhough objects and tile_bin and if the point is in the
        bounds set moving true and if the item is in the bin remove it from the
        list

        if the mouse wheel button is released set the boolean flag

        if the wheel is scrolled notify the relavant bin."""
        if(button == 1):
            if(self.selected != None):
                #test if the item is in either bin
                if(self.object_bin.rect.colliderect(self.selected.rect) or
                   self.tile_bin.rect.colliderect(self.selected.rect)):
                    self.selected = None;
                elif(type(self.selected) is GameObject):
                    if(self.selected.in_bin):
                        self.selected.in_bin = False;
                        self.selected.rect.x -= self.x_offset;
                        self.selected.rect.y -= self.y_offset;
                    self.objects.append(self.selected);
                    self.selected = None;
                elif(type(self.selected) is Tile):
                    point = list(point);
                    point[0] -= self.x_offset;
                    point[1] -= self.y_offset;

                    for row in self.tiles:
                        for item in row:
                            if(item.rect.collidepoint(point)):
                                item.color = self.selected.color;
                                item.path = self.selected.path;



                    self.selected = None;
                else:
                    self.selected = None;
        elif(button == 2):
            self.scrolling = False;
        elif(button == 5):
            if(self.object_bin.contains_point(point)):
                self.object_bin.scroll_down();
            elif(self.tile_bin.contains_point(point)):
                self.tile_bin.scroll_down();


