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

# ---------------------------
# classes
# ---------------------------

class Entity:
    # this is a generic object: the play, a monster, an iem, the stairs
    # it's always represented by a character on screen
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by the given amount
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
player = Entity(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', libtcod.white)
#object that represents an npc
npc =  Entity(SCREEN_WIDTH / 2 -5, SCREEN_HEIGHT / 2 - 5, '@', libtcod.yellow)

# the list of objects with these in them
objects = [npc, player]


# ---------------------------
# main game loop
# ---------------------------
while not libtcod.console_is_window_closed():

    # draw all objects in the list
    for entity in objects:
        entity.draw()

    # transfer everything from con to the root console and present it
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    # clear all object before they move
    for entity in objects:
        entity.clear()

    # handle key press now
    exit = handle_keys()
    if exit:
        break


# -- end of the main program
