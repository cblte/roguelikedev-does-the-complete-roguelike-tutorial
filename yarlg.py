#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
#title           : yarlg.py
#description     : YetAnotherRogueLikeGame
#author          : cblte
#date            : 2017-08-20
#version         : 0.2
#usage           : python pyscript.py
#notes           : Part 2 - the object and the map
#python_version  : 2.x
#==============================================================================

import libtcodpy as libtcod

# actual size of the window and main game settings
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20 # 20 FPS maximum

MAP_WIDTH = 80
MAP_HEIGHT = 45
color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)


# ---------------------------
# classes
# ---------------------------

class Tile:
    # a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        # by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

# ----- END OF TILE class


class Object:
    # this is a generic object: the play, a monster, an iem, the stairs
    # it's always represented by a character on screen
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by the given amount
        if not map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self):
        # set the color and then draw the character that represents
        # this object at its position
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self):
        # erase the character that represents this object
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
## ----- END OF Object



# ---------------------------
# functions
# ---------------------------

def make_map():
    global map

    # fill map with unblocked tiles
    map = [[ Tile(False)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]

            # place two pillars to test the map
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[50][22].blocked = True
    map[50][22].block_sight = True


# ----- end of make_map

def render_all():
    # render the map, then put everything else on top if that

    global color_light_wall
    global color_Light_ground

    # draw the map
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, color_dark_ground)

    # draw all objects in the list
    for object in objects:
        object.draw()

    # transfer everything from con to the root console and present it
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# ----- end of render_all


def handle_keys():
    # function to handle key input and to move the player around
    key = libtcod.console_check_for_keypress()

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # ALT+Enter : toggle Fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True     # exit the game

    # movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0,-1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1,0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0,1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,0)

# ----- end of handle_keys


# ---------------------------
# initilizion & main loop
# ---------------------------
# setting the font
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'RLD_DTC_RLT - YetAnotherRogueLikeGame',False)
libtcod.sys_set_fps(LIMIT_FPS)
# off screen console
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

# object that represents the player
player = Object(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', libtcod.white)
#object that represents an npc
npc =  Object(SCREEN_WIDTH / 2 -5, SCREEN_HEIGHT / 2 - 5, '@', libtcod.yellow)

# the list of objects with these in them
objects = [npc, player]

# generate map (at this point it is not drawn to the screen)
make_map()

# ---------------------------
# main game loop
# ---------------------------
while not libtcod.console_is_window_closed():

    # render the screen
    render_all()

    libtcod.console_flush()

    # clear all object before they move
    for Object in objects:
        Object.clear()

    # handle key press now
    exit = handle_keys()
    if exit:
        break


# -- end of the main program
