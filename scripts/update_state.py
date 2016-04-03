__author__ = 'Perkel'
import pygame as pg


def keyboard_system_events():
    import storage as st
    keylist = []

    # checking input from keyboard
    if st.Input.keys_pressed[pg.K_LALT]:
        keylist.append('LALT')
    if st.Input.keys_pressed[pg.K_F4]:
        keylist.append('F4')
    if st.Input.keys_pressed[pg.K_RETURN]:
        keylist.append('ENTER')

    # adding events based on input
    if 'LALT' in keylist and 'F4' in keylist:
        st.Events.system.append('QUIT')
    if 'LALT' in keylist and 'ENTER' in keylist:
        if st.Display.fullscreen is True:
            st.Events.system.append('DISPLAY:WINDOWED')
        else:
            st.Events.system.append('DISPLAY:FULLSCREEN')


def handle_system_events():
    import storage as st
    # KEYBOARD BASED EVENTS
    for event in st.Events.system:
        if event == 'QUIT':
            st.System.isGameStillRunning = False
        if event == 'DISPLAY:FULLSCREEN':
            st.Display.fullscreen = True
        if event == 'DISPLAY:WINDOWED':
            st.Display.fullscreen = False

    # DISPLAY
