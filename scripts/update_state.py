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


def handle_events_ui_game():

    """

    This handles ui events like changing ui elements, navigating menus etc.
    :return:

    """

    import storage as st
    import scripts.ui.ui_storage as ui_storage

    for event in st.Events.game:

        # ||||||||||   EVENTS - MAIN MENU   |||||||||||

        # CONTINUE BUTTON
        # NEW GAME BUTTON

        if event == 'EVENT:main_menu:start_new_game':
            st.System.newGameStarted = True
            ui_storage.UIPlayerCreation.input_control = True
            ui_storage.UIPlayerCreation.visible = True
            ui_storage.UIMainMenu.input_control = False
            ui_storage.UIMainMenu.visible = False
            print "started new game"

        # SAVE BUTTON
        # LOAD BUTTON
        # OPTIONS BUTTON

        elif event == 'EVENT:main_menu:options_on':
            ui_storage.UIMainMenu.input_control = False
            ui_storage.UIMainMenu.visible = False
            ui_storage.UIOptions.input_control = True
            ui_storage.UIOptions.visible = True
            print "switch on options menu"

        # QUIT BUTTON
        elif event == 'EVENT:main_menu:quit':
            st.System.isGameStillRunning = False

        # ||||||||||   EVENTS - CHARACTER CREATOR   |||||||||||

        elif event == 'EVENT:char_creator:next_face':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIPlayerCreation.face_count < len(ui_storage.UIPlayerCreation.list_faces)-1:
                ui_storage.UIPlayerCreation.face_count += 1
                print "current face: ", ui_storage.UIPlayerCreation.face_count
            else:
                ui_storage.UIPlayerCreation.face_count = 0
                print "current face: ", ui_storage.UIPlayerCreation.face_count

        elif event == 'EVENT:char_creator:previous_face':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIPlayerCreation.face_count <= 0:
                ui_storage.UIPlayerCreation.face_count = len(ui_storage.UIPlayerCreation.list_faces)-1
                print "current face: ", ui_storage.UIPlayerCreation.face_count
            else:
                ui_storage.UIPlayerCreation.face_count -= 1
                print "current face: ", ui_storage.UIPlayerCreation.face_count

        elif event == 'EVENT:char_creator:next_face_background':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIPlayerCreation.face_background_count < len(ui_storage.UIPlayerCreation.list_background)-1:
                ui_storage.UIPlayerCreation.face_background_count += 1
                print "current face background: ", ui_storage.UIPlayerCreation.face_background_count
            else:
                ui_storage.UIPlayerCreation.face_background_count = 0
                print "current face background: ", ui_storage.UIPlayerCreation.face_background_count

        elif event == 'EVENT:char_creator:previous_face_background':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIPlayerCreation.face_background_count <= 0:
                ui_storage.UIPlayerCreation.face_background_count = len(ui_storage.UIPlayerCreation.list_background)-1
                print "current face background: ", ui_storage.UIPlayerCreation.face_background_count
            else:
                ui_storage.UIPlayerCreation.face_background_count -= 1
                print "current face background: ", ui_storage.UIPlayerCreation.face_background_count

        # |||||||||||||        EVENTS : OPTIONS MENU         ||||||||||||||||||||

        # changing pages in ui options
        elif event == 'EVENT:ui_options:change_screen_game':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIOptions.submenu_game_visible is False:
                ui_storage.UIOptions.submenu_game_visible = True
                ui_storage.UIOptions.submenu_display_visible = False
                ui_storage.UIOptions.submenu_sound_visible = False

        elif event == 'EVENT:ui_options:change_screen_display':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIOptions.submenu_display_visible is False:
                ui_storage.UIOptions.submenu_game_visible = False
                ui_storage.UIOptions.submenu_display_visible = True
                ui_storage.UIOptions.submenu_sound_visible = False
        elif event == 'EVENT:ui_options:change_screen_sound':
            import scripts.ui.ui_storage as ui_storage
            if ui_storage.UIOptions.submenu_sound_visible is False:
                ui_storage.UIOptions.submenu_display_visible = False
                ui_storage.UIOptions.submenu_game_visible = False
                ui_storage.UIOptions.submenu_sound_visible = True
        elif event == 'EVENT:ui_options:options_off':
            ui_storage.UIMainMenu.input_control = True
            ui_storage.UIMainMenu.visible = True
            ui_storage.UIOptions.input_control = False
            ui_storage.UIOptions.visible = False

            ui_storage.UIOptions.submenu_game_visible = False
            ui_storage.UIOptions.submenu_display_visible = False
            ui_storage.UIOptions.submenu_sound_visible = False
            print "close options menu"

        # events in game submenu
        # events in display submenu
        elif event == 'EVENT:ui_options:display:fullscreen_switch':
            if ui_storage.UIOptions.ui_sub_display_fullscreen is False:
                st.Events.system.append('DISPLAY:FULLSCREEN')
                ui_storage.UIOptions.ui_sub_display_fullscreen = True
                import scripts.ui.menu_options as mo
                ui_storage.UIOptions.button_display_mode = mo.MenuOptions.UIButtonDisplaySetMode(
                    ui_storage.UIOptions.image_button_switch_on)
            else:
                st.Events.system.append('DISPLAY:WINDOWED')
                ui_storage.UIOptions.ui_sub_display_fullscreen = False
                import scripts.ui.menu_options as mo
                ui_storage.UIOptions.button_display_mode = mo.MenuOptions.UIButtonDisplaySetMode(
                    ui_storage.UIOptions.image_button_switch_off)
        # events in sound submenu

        else:
            pass
    # Clearing events list
    st.Events.game = []

