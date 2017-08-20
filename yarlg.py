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

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20 # 20 FPS maximum

# setting the font
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# most important call, initilizing the window
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'RLD_DTC_RLT - YetAnotherRogueLikeGame',False)
# this is just for a real time based game
libtcod.sys_set_fps(LIMIT_FPS)

# player setup
playerx = SCREEN_WIDTH / 2
playery = SCREEN_HEIGHT / 2

#
# function to handle key input and to move the player around
# v 1
def handle_keys():
    global playerx
    global playery

    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # ALT+Enter : toggle Fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True     # exit the game

    # movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1

# ----- end of handle_keys


# now the main loop of the game
while not libtcod.console_is_window_closed():
    # off screen console
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    # each iteration we want to print something usefull to the screen
    # turn based: each iteration is a turn. real-time each one is a frame
    libtcod.console_set_default_foreground(con, libtcod.white)

    # now we print a character at position 1,1
    libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)

    # transfer everything from con to the root console
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    # flush everything to the front
    libtcod.console_flush()

    # delete "old" player position
    libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)
    # handle key press now
    exit = handle_keys()
    if exit:
        break
