"""main.py
    create and maintain the main loop for pygame and be the starting point for
    the program
"""

import pygame, sys;
pygame.init();
from map import Map;

def main():
    main_loop();

def main_loop():
    size = width, height = 750, 450;
    black = 0, 0, 0;

    #build screen and set boolean flag traking the state of the program to True
    screen = pygame.display.set_mode(size);
    running = True;

    #Build the map to store and handle all information
    map = Map();

    while running:
        #go through events and if it is a quit event exit or if it is a mouse
        #~down or up event pass it along to the map
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
               running = False;
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                map.mouse_down(event.pos, event.button);
            elif(event.type == pygame.MOUSEBUTTONUP):
                map.mouse_up(event.pos, event.button);


        #update objects
        map.update();

        #render
        screen.fill(black);
        map.draw(screen);
        pygame.display.flip();


if(__name__ == '__main__'):
    main();
