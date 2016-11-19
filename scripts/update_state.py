__author__ = 'Perkel'
import pygame as pg


def ui_main_ui_logic():
    import scripts.ui.ui_objects as ui_objects
    for menu in ui_objects.ui_main_list:
        menu.menu_logic()


def keyboard_system_events():
    import storage as st

    # adding events based on input
    if st.Input.keys_pressed[pg.K_LALT] and st.Input.keys_pressed[pg.K_F4]:
        st.Events.system.append('QUIT')
    if st.Input.keys_pressed[pg.K_LALT] and st.Input.keys_pressed[pg.K_RETURN]:
        if st.Display.fullscreen is True:
            st.Events.system.append('DISPLAY:WINDOWED')
        else:
            st.Events.system.append('DISPLAY:FULLSCREEN')


def handle_system_events():
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


def handle_events_game():
    import storage as st
    for event in st.Events.game:
        if event == 'EVENT:NEWGAME':
            st.System.newGameStarted = True
            import scripts.ui.ui_storage as ui_storage
            ui_storage.UIPlayerCreation.input_control = True
            ui_storage.UIPlayerCreation.visible = True
            ui_storage.UIMainMenu.input_control = False
            ui_storage.UIMainMenu.visible = False
            print " NEW GAME STARTED !"