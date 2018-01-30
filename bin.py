"""bin.py
    store a list of objects for the user to select from
"""

from pygame import Rect, draw;

class Bin(object):

    COLOR = (150, 150, 150);
    PADDING = 7;
    IMAGE_WIDTH = 64;
    IMAGE_HEIGHT = 64;
    VEL_Y = 8;

    def __init__(self, x, y, width, height):
        self._rect = Rect(x, y, width, height);
        self._objects = [];
        self._y_offset = 0;

    @property
    def rect(self):
        '''store the position and dimenstions of the binn and handle
        collisionfs'''
        return self._rect;

    @property
    def objects(self):
        '''hold any items in the bin'''
        return self._objects;

    @property
    def y_offset(self):
        '''store the offset required in order to scroll'''
        return self._y_offset;

    @y_offset.setter
    def y_offset(self, y_offset):
        self._y_offset = y_offset;

    def add_item(self, item):
        """add item to the object list modifying its cooridinates in order dor
        the map ."""
        multiplier_x = len(self.objects) % 2;
        multiplier_y = len(self.objects) / 2;

        item.rect.x = (self.PADDING + (self.IMAGE_WIDTH + self.PADDING) *
                       multiplier_x + self.rect.x);

        item.rect.y = (self.PADDING + (self.IMAGE_HEIGHT + self.PADDING) *
                      multiplier_y + self.rect.y);

        self.objects.append(item);

    def remove_item(self, item):
        """remove item from the _objects list"""
        self.objects.remove(item);

    def contains_point(self, point):
        """return boolean if the point is in the rectangle"""
        return self.rect.collidepoint(point);

    def in_bin(self, item):
        """return boolean if the item is in self.rect which represents the
        bin"""
        return self.rect.contains(item.rect);

    def draw_items(self, screen, x_offset = 0, y_offset = 0):
        """draw the items in _objects"""
        draw.rect(screen, self.COLOR, self.rect);
        for item in self.objects:
            item.draw(screen, y_offset =  self.y_offset);

    def mouse_down(self, point):
        for item in self.objects:
            if(item.contains_point(point)):
                new_item = item.copy();
                new_item.moving = True;
                return new_item;
        return None;

    def scroll_down(self):
        predict_offset = self.y_offset - self.VEL_Y;
        if(self.objects[len(self.objects) - 1].rect.bottom + predict_offset <
           self.rect.bottom):
            return;
        self.y_offset = predict_offset;

    def scroll_up(self):
        """called when the wheel is scrolled up and causes the items to move
        down by increasing the y_offset"""
        predict_offset = self.y_offset + self.VEL_Y;
        if(self.objects[0].rect.top + predict_offset > self.rect.top):
            return;
        self.y_offset = predict_offset;
