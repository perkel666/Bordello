__author__ = 'Perkel'

import pygame as pg


def mouse_input():
    mouse_buttons = pg.mouse.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    return mouse_buttons, mouse_pos


def keyboard_input():
    keys = pg.key.get_pressed()
    return keys