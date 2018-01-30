"""button.py
    allow the a button to be drawn to the screen and be clicked on
"""

from pygame import font, Rect, draw;

class Button(object):

    def __init__(self, text, x, y, command):

        myFont = font.SysFont(None, 21);
        self._text = myFont.render(text, 1, (0, 0, 0));
        self._rect = Rect(x, y, self.text.get_width(), self.text.get_height());
        self._command = command;
        self._color = (255, 255, 255);

    @property
    def text(self):
        '''the text to be displayed by the button'''
        return self._text

    @text.setter
    def text(self, text):
        myFont = font.SysFont(None, 21);
        self._text = myFont.render(text, 1, (0, 0, 0));

    @property
    def rect(self):
        '''a pygamerect to represent the position and dimenstions of the
        button'''
        return self._rect;

    @property
    def command(self):
        '''the function to be called whenthe button is pressed'''
        return self._command;

    @command.setter
    def command(self, command):
        self._command = command;

    @property
    def color(self):
        '''color of the border and background'''
        return self._color;

    @color.setter
    def color(self, color):
        self._color = color;

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect);
        screen.blit(self.text, (self.rect.x, self.rect.y));

    def click(self):
        self.command();

