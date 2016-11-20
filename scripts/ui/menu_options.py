__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuOptions():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage

        # UI INITIALIZATION
                    # main options menu
        self.ui_transparency = MenuOptions.UITransparency(
            ui_storage.UIOptions.image_ui_transparency)
        self.ui_background = MenuOptions.UIBackground(
            ui_storage.UIOptions.image_ui_main_background)
                    # buttons main
        self.ui_button_game = MenuOptions.UIButtonGame(
            ui_storage.UIOptions.image_button_game)
        self.ui_button_display = MenuOptions.UIButtonDisplay(
            ui_storage.UIOptions.image_button_display)
        self.ui_button_sound = MenuOptions.UIButtonSound(
            ui_storage.UIOptions.image_button_sound)
        self.ui_button_back = MenuOptions.UIButtonBack(
            ui_storage.UIOptions.image_button_back)
                    # buttons in display option
        self.ui_button_display_set_mode = MenuOptions.UIButtonDisplaySetMode(
            ui_storage.UIOptions.image_button_display_set_mode)
                    # background submenus
        self.ui_submenu_game = MenuOptions.UIGameBackground(
            ui_storage.UIOptions.image_ui_game_background)
        self.ui_submenu_display = MenuOptions.UIDisplayBackground(
            ui_storage.UIOptions.image_ui_display_background)
        self.ui_submenu_sound = MenuOptions.UISoundBackground(
            ui_storage.UIOptions.image_ui_sound_background)
                    # lists
        self.ui_buttons_list = [
            self.ui_button_game,
            self.ui_button_display,
            self.ui_button_sound,
            self.ui_button_back]

        self.ui_submenus_list = [
            self.ui_submenu_game,
            self.ui_submenu_display,
            self.ui_submenu_sound]

        self.menu_background_visible_list = []
        self.menu_buttons_visible_list = []

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import storage as st

        if ui_storage.UIOptions.visible is True:

            self.menu_background_visible_list = []
            self.menu_buttons_visible_list = []

            self.ui_background.rect.x = ui_storage.UIOptions.position[0]
            self.ui_background.rect.y = ui_storage.UIOptions.position[1]

            self.ui_button_display_set_mode.rect.x = ui_storage.UIOptions.position_submenu_button_display_mode[0]
            self.ui_button_display_set_mode.rect.y = ui_storage.UIOptions.position_submenu_button_display_mode[1]

            for menu in self.ui_submenus_list:
                menu.rect.x = ui_storage.UIOptions.position_submenu[0]
                menu.rect.y = ui_storage.UIOptions.position_submenu[1]

            for button in self.ui_buttons_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            difference = 0  # initial difference
            for button in self.menu_buttons_visible_list:
                button.rect.x = ui_storage.UIOptions.position_buttons[0]
                button.rect.y = ui_storage.UIOptions.position_buttons[1] + difference
                difference += ui_storage.UIOptions.buttons_y_difference


    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        if ui_storage.UIOptions.visible is True:

            layer_menu_options_background = pg.sprite.Group()
            layer_menu_options_ui_background = pg.sprite.Group()
            layer_menu_options_buttons = pg.sprite.Group()
            layer_menu_options_body_background = pg.sprite.Group()
            layer_menu_options_body_buttons = pg.sprite.Group()

            if self.ui_submenu_game.visible:
                layer_menu_options_body_buttons.add(self.ui_button_display_set_mode)

            for button in self.ui_buttons_list:
                if button.visible:
                    layer_menu_options_buttons.add(button)

            layer_menu_options_background.add(self.ui_transparency)
            layer_menu_options_ui_background.add(self.ui_background)
            for body in self.ui_submenus_list:
                if body.visible:
                    layer_menu_options_body_background.add(body)

            layer_menu_options_background.draw(storage.Display.screen)
            layer_menu_options_ui_background.draw(storage.Display.screen)
            layer_menu_options_buttons.draw(storage.Display.screen)
            layer_menu_options_body_background.draw(storage.Display.screen)
            layer_menu_options_body_buttons.draw(storage.Display.screen)

    def execute_actions(self):
        import scripts.ui.ui_storage as ui_storage
        # GETTING STATE OF BUTTONS
        if ui_storage.UIOptions.input_control is True:
            for button in self.ui_buttons_list:
                button.get_state()
            if self.ui_button_display_set_mode.visible is True:   # NEED TO BE REFACTORED
                self.ui_button_display_set_mode.get_state()

        # EXECUTING BUTTONS STATES
        if ui_storage.UIOptions.input_control is True:
            for button in self.ui_buttons_list:
                button.do_action()
            if self.ui_button_display_set_mode.visible is True:   # NEED TO BE REFACTORED
                self.ui_button_display_set_mode.do_action()

    ##################################
    # CLASSES used in OptionsMenu() #
    ##################################

        # first screen
    class UITransparency(Button):
        def __init__(self, name):
            super(MenuOptions.UITransparency, self).__init__(name)

    class UIBackground(Button):
        def __init__(self, name):
            super(MenuOptions.UIBackground, self).__init__(name)

        # buttons main
    class UIButtonGame(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonGame, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False

    class UIButtonDisplay(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonDisplay, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False

    class UIButtonSound(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonSound, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False

    class UIButtonBack(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonBack, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            import scripts.ui.ui_storage as ui_storage
            import storage as st
            import time
            if self.last_pressed is True:
                print "back"
                st.Events.game.append('EVENT:main_menu:options_off')
                self.last_pressed = False

    class UIButtonDisplaySetMode(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonDisplaySetMode, self).__init__(name, hover=True)
            self.visible = False
            self.image_on = Button('button_state_on.png', hover=True)
            self.image_off = Button('button_state_off.png', hover=True)
            self.on = False

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False

        # background to option right screens

    class UIGameBackground(Button):
        def __init__(self, name):
            super(MenuOptions.UIGameBackground, self).__init__(name)
            self.visible = True

    class UIDisplayBackground(Button):
        def __init__(self, name):
            super(MenuOptions.UIDisplayBackground, self).__init__(name)
            self.visible = False

    class UISoundBackground(Button):
        def __init__(self, name):
            super(MenuOptions.UISoundBackground, self).__init__(name)
            self.visible = False