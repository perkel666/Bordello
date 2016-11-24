__author__ = 'Perkel'
import pygame as pg


def ui_main_ui_logic():
    """
    This iteration over list created in ui_objects.py and defacto what creates UI elements
    which are used in main loop
    """
    import scripts.ui.ui_objects as ui_objects
    for menu in ui_objects.ui_main_list:
        menu.menu_logic()


def ui_execute_ui_logic():
    """
    This executes stuff post rendering of ui elements. Mostly cleanup of weird bugs
    that can happen when you execute stuff before drawing on screen stuff.
    """
    import scripts.ui.ui_objects as ui_objects
    for menu in ui_objects.ui_main_list:
        menu.execute_actions()


# EVENTS CREATION


def keyboard_system_events():
    """
    This creates events from keyboard input
    :return:
    """
    import storage as st
    # adding events based on input
    if st.Input.keys_pressed[pg.K_LALT] and st.Input.keys_pressed[pg.K_F4]:
        st.Events.system.append('QUIT')
    if st.Input.keys_pressed[pg.K_LALT] and st.Input.keys_pressed[pg.K_RETURN]:
        if st.Display.fullscreen is True:
            st.Events.system.append('DISPLAY:WINDOWED')
        else:
            st.Events.system.append('DISPLAY:FULLSCREEN')


# EVENTS HANDLING


def handle_system_events():
    """
    This handles system events like Quit game and other.
    :return:
    """
    import storage as st
    for event in st.Events.system:
        if event == 'QUIT':
            st.System.isGameStillRunning = False
        if event == 'DISPLAY:FULLSCREEN':
            st.Display.fullscreen = True
        if event == 'DISPLAY:WINDOWED':
            st.Display.fullscreen = False
        if event == 'PRINT:FILELIST':
            st.Files.files.print_file_list()

    # DISPLAY FULL-SCREEN SWITCH
    if st.Display.fullscreen_switch != st.Display.fullscreen:
        if st.Display.fullscreen is True:
            pg.display.set_mode(st.Display.resolution, pg.FULLSCREEN)
            st.Display.fullscreen_switch = st.Display.fullscreen
        else:
            pg.display.set_mode(st.Display.resolution)
            st.Display.fullscreen_switch = st.Display.fullscreen

    st.Events.system = []
