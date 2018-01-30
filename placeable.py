"""placeable.py
    serve as an abstract base class for anything that is placeable to the
    screen.
"""
import abc;

class Placeable(object):
    __metaclass__ = abc.ABCMeta;

    def __init__(self, image_path):
        self._path = image_path;
        self._moving = False;
        self._in_bin = True;
        self._rect = None;

    @property
    def path(self):
        '''the path to the image corresponding to teh placeable pbject'''
        return self._path;

    @property
    def moving(self):
        '''boolean flag storing whether the object is moving or not'''
        return self._moving;

    @moving.setter
    def moving(self, moving):
        self._moving = moving;

    @property
    def in_bin(self):
        '''boolean flag storing whether the item is currently stored in its
        bin'''
        return self._in_bin;

    @in_bin.setter
    def in_bin(self, in_bin):
        self._in_bin = in_bin;


    @property
    def rect(self):
        '''pygame rect storing the [positionand  dimensions'''
        return self._rect;

    @rect.setter
    def rect(self, rect):
        self._rect = rect;

    def move(self, dx, dy):
        """move the object by the change in x and y denoted by dx and dy"""
        self.rect = self.rect.move(dx, dy);

    def contains_point(self, point):
        """check to see if the image_rect contains the given point"""
        return self.rect.collidepoint(point);

    @abc.abstractmethod
    def draw(self, screen, x_offset = 0, y_offset = 0):
        """draw the placeable item to the screen using the offsets and placing
        it at self.rect"""
        return;

    @abc.abstractmethod
    def copy(self):
        """return a copy of the Placeable item"""
        return;


