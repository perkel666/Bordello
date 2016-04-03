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

    # checking input from keyboard
    if st.Input.keys_pressed[pg.K_LALT]:
        st.Input.all_input.append('LALT')
    if st.Input.keys_pressed[pg.K_F4]:
        st.Input.all_input.append('F4')
    if st.Input.keys_pressed[pg.K_RETURN]:
        st.Input.all_input.append('ENTER')