"""game-object.py
    store the information for each object that can be placed on the map
"""

from placeable import Placeable;
from pygame import image;

class GameObject(Placeable):

    def __init__(self, image_path):
        Placeable.__init__(self, image_path);

        #store the image to be represented
        self._image = image.load(self.path);

        #build the rectangle for the image
        self.rect = self.image.get_rect();

        #default to in the bin
        self.in_bin = True;


    @property
    def image(self):
        return self._image;

    def draw(self, screen, x_offset = 0, y_offset = 0):
        """draw the image to the screen at the image_rect position and
        bounds"""
        rect = self.rect.copy();
        #f(not self.in_bin):
        rect.x += x_offset;
        rect.y += y_offset;
        screen.blit(self.image, rect);

    def copy(self):
        """return a copy of the GameObject"""
        item = GameObject(self.path);
        item.rect.x = self.rect.x;
        item.rect.y = self.rect.y;
        return item;
