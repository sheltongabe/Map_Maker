"""tile.py
    store the information for each tile in the background
"""

from placeable import Placeable;
from pygame import Rect;
from pygame import draw;
from pygame import image;

class Tile(Placeable):

    WIDTH, HEIGHT = 50, 50;

    def __init__(self, image_path, color = (0, 0, 0), x = 0, y = 0):
        Placeable.__init__(self, image_path);

        #define path to the image
        self._path = image_path;

        #define the color for the tile to represent
        self._color = color

        self._image = image.load(image_path);

        #a rectangle to store the position of the tile
        self._rect = Rect(x, y, self.WIDTH, self.HEIGHT);

    @property
    def color(self):
        return self._color;

    @color.setter
    def color(self, color):
        self._color = color;

    @property
    def path(self):
        return self._path;

    @path.setter
    def path(self, path):
        self._path = path;

        self.image = image.load(path);

    @property
    def image(self):
        return self._image;

    @image.setter
    def image(self, image):
        self._image = image;


    def draw(self, screen, x_offset = 0, y_offset = 0):
        """draw the tile to the screen using the given color"""
        #draw.rect(screen, self.color, self.rect);
        rect = self.rect.copy();
        if(not self.in_bin):
            rect.x += x_offset;
            rect.y += y_offset;
        screen.blit(self.image, rect);
    def copy(self):
        """return a new Tile using the properties of this tile"""
        item = Tile(self.path, self.color, self.rect.x, self.rect.y);

        return item;

