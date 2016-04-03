__author__ = 'Perkel'

import pygame as pg
import storage as st


def mouse_input():
    st.Input.mouse_pressed_buttons = pg.mouse.get_pressed()
    st.Input.mouse_pos = pg.mouse.get_pos()


def keyboard_input():
    st.Input.keys_pressed = pg.key.get_pressed()