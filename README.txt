Map maker is a program writen in python designed to allow for the rapid building of a 2d world for purposes in game
development.

Setup:
first you must install pygame and can do so by using pip or if you are using debian based system you should be able to
insall it through the repositoory.
ex: 
pip$ pip install pygame
debian$ atp-get install python-pygame

Following this you simply download and place the directory /Map-Maker wherever you like, navigate into it and run it in
python2 witht he following command.

$ python main.py

main.py is the starting point of the program and is where the pygame instance is given substance and handles the main
loop.


Adding images:
in order to add your own images you simply must place objects in the resources/objects folder and terrain into
resoureces/terrain.

they prefer .png format in the follwoing sizes:
object: 64x64
tile: 50x50 | if you would like to change this you must change it for all tiles and adjust the constants in the Tile
              class

Simply drag images from the gray filled bins onto the map in the center to build a map and use the save and load buttons
to persist.  The .map extension is recommended however completely optional.
And you can hold down on the mouse button to pan the map accross the screen.

art credits: from www.opengameart.org
house0.png, house1.png -> Shepardskin
hunter0.png, pavilion0.png, lumberjack0.png, storage0.png -> Unknown Horizons
tent0.png -> Unknown Horizons
tree0.png, tree1.png -> ansimuz
tree_dead0.png -> J-Robot

all terrain tiles -> CryHam
