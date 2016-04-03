__author__ = 'Perkel'

import pygame as pg


def mouse_input():
    import storage as st
    st.Input.mouse_pressed_buttons = pg.mouse.get_pressed()
    st.Input.mouse_pos = pg.mouse.get_pos()


def keyboard_input():
    import storage as st
    st.Input.keys_pressed = pg.key.get_pressed()
    st.Input.all_input = []