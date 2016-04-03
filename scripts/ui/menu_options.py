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

            # CREATING VISIBLE BUTTONS LIST
            for button in self.ui_buttons_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            # CREATING VISIBLE RIGHT MENU LIST
            for button in self.ui_buttons_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            # POSITIONING BUTTONS ON MAIN MENU
            difference = 0  # initial difference
            for button in self.menu_buttons_visible_list:
                button.rect.x = ui_storage.UIOptions.position_buttons[0]
                button.rect.y = ui_storage.UIOptions.position_buttons[1] + difference
                difference += ui_storage.UIOptions.buttons_y_difference

                        # buttons
            if ui_storage.UIOptions.input_control:
                for button in self.ui_buttons_list:
                    button.get_state()

            if game.input_control is "options_menu":
                if self.ui_button_display_set_mode.visible is True:
                    self.ui_button_display_set_mode.get_state(game)

            # OUTPUT
            if game.input_control is "options_menu":
                for button in self.ui_buttons_list:
                    button.do_action(game)

            if self.ui_submenu_display.visible is True:
                self.ui_button_display_set_mode.visible = True

            if game.input_control is "options_menu":
                if self.ui_button_display_set_mode.visible is True:
                    self.ui_button_display_set_mode.do_action(game)

            # ADD SPRITES TO LAYERS

            for submenu in self.ui_submenus_list:
                if submenu.visible is True:
                    layer_submenus.add(submenu)

            if self.ui_button_display_set_mode.visible is True:
                layer_submenu_buttons.add(self.ui_button_display_set_mode)

            for button in self.ui_buttons_list:
                if button.visible is True:
                    layer_buttons_top.add(button)


    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        if ui_storage.UIMainMenu.visible is True:

            layer_menu_options_background = pg.sprite.Group()
            layer_menu_options_ui_background = pg.sprite.Group()
            layer_menu_options_buttons = pg.sprite.Group()
            layer_menu_options_body_background = pg.sprite.Group()
            layer_menu_options_body_buttons = pg.sprite.Group()

            # ADD SPRITES TO LAYERS
            for background in self.menu_background_visible_list:
                layer_main_menu_background.add(background)

            for button in self.menu_buttons_visible_list:
                layer_main_menu_buttons.add(button)

            if self.background_ui.visible is True:
                layer_main_menu_ui_graphic.add(self.background_ui)

            # DISPLAY LAYERS
            layer_main_menu_background.draw(storage.Display.screen)
            layer_main_menu_ui_graphic.draw(storage.Display.screen)
            layer_main_menu_buttons.draw(storage.Display.screen)

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
            if self.last_pressed is True:
                self.last_pressed = False

                # buttons display

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