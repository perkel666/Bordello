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

        # buttons in display option submenu
        self.ui_button_display_set_mode = MenuOptions.UIButtonDisplaySetMode(
            ui_storage.UIOptions.image_button_display_set_mode)

        # background submenus
        self.ui_submenu_game_background = MenuOptions.UIGameBackground(
            ui_storage.UIOptions.image_ui_game_background)
        self.ui_submenu_display_background = MenuOptions.UIDisplayBackground(
            ui_storage.UIOptions.image_ui_display_background)
        self.ui_submenu_sound_background = MenuOptions.UISoundBackground(
            ui_storage.UIOptions.image_ui_sound_background)

        # ADDING OBJECTS TO LISTS
        self.ui_buttons_list = [
            self.ui_button_game,
            self.ui_button_display,
            self.ui_button_sound,
            self.ui_button_back]

        ui_storage.UIOptions.submenu_list = [
            self.ui_submenu_game_background,
            self.ui_submenu_display_background,
            self.ui_submenu_sound_background]

        self.ui_submenu_game_button_list = []

        self.ui_submenu_display_button_list = [
            self.ui_button_display_set_mode]

        self.ui_submenu_sound_button_list = []

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import storage as st

        if ui_storage.UIOptions.visible is True:

            menu_background_visible_list = []
            submenus_visible_list_ = []
            menu_buttons_visible_list = []

            # POSITIONING
            # background
            self.ui_background.rect.x = ui_storage.UIOptions.position[0]
            self.ui_background.rect.y = ui_storage.UIOptions.position[1]
            # buttons main
            difference = 0  # initial difference
            for button in self.ui_buttons_list:
                button.rect.x = ui_storage.UIOptions.position_buttons[0]
                button.rect.y = ui_storage.UIOptions.position_buttons[1] + difference
                difference += ui_storage.UIOptions.buttons_y_difference
            # options submenu background
            for menu in ui_storage.UIOptions.submenu_list:
                menu.rect.x = ui_storage.UIOptions.position_submenu[0]
                menu.rect.y = ui_storage.UIOptions.position_submenu[1]
            # options submenu buttons
            self.ui_button_display_set_mode.rect.x = ui_storage.UIOptions.position_submenu_button_display_mode[0]
            self.ui_button_display_set_mode.rect.y = ui_storage.UIOptions.position_submenu_button_display_mode[1]

            for button in self.ui_buttons_list:
                if button.visible is True:
                    menu_buttons_visible_list.append(button)

    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        if ui_storage.UIOptions.visible is True:

            # CREATING SPRITE GROUPS

            layer_menu_options_background = pg.sprite.Group()
            layer_menu_options_transparency = pg.sprite.Group()
            layer_menu_options_ui_background = pg.sprite.Group()
            layer_menu_options_buttons = pg.sprite.Group()
            layer_menu_options_submenu_background = pg.sprite.Group()
            layer_menu_options_submenu_buttons = pg.sprite.Group()

            # ADDING SPIRITES TO SPRITE GROUPS

            # background
            layer_menu_options_background.add(self.ui_background)
            # transparency
            layer_menu_options_transparency.add(self.ui_transparency)
            # Options UI background
            layer_menu_options_ui_background.add(self.ui_background)
            # Options UI buttons
            for button in self.ui_buttons_list:
                if button.visible is True:
                    layer_menu_options_buttons.add(button)
            # Options UI submenu background
            if ui_storage.UIOptions.submenu_display_visible is True:
                layer_menu_options_submenu_background.add(self.ui_submenu_display_background)
            if ui_storage.UIOptions.submenu_game_visible is True:
                layer_menu_options_submenu_background.add(self.ui_submenu_game_background)
            if ui_storage.UIOptions.submenu_sound_visible is True:
                layer_menu_options_submenu_background.add(self.ui_submenu_sound_background)
            # Options UI submenu buttons
            if ui_storage.UIOptions.submenu_display_visible is True:
                for button in self.ui_submenu_display_button_list:
                    layer_menu_options_submenu_buttons.add(button)

            # DRAWING SPRITE GROUPS IN LAYERS
            layer_menu_options_background.draw(storage.Display.screen)
            layer_menu_options_transparency.draw(storage.Display.screen)
            layer_menu_options_ui_background.draw(storage.Display.screen)
            layer_menu_options_buttons.draw(storage.Display.screen)
            layer_menu_options_submenu_background.draw(storage.Display.screen)
            layer_menu_options_submenu_buttons.draw(storage.Display.screen)

    def execute_actions(self):
        import scripts.ui.ui_storage as ui_storage
        # GETTING STATE OF BUTTONS
        if ui_storage.UIOptions.input_control is True:
            for button in self.ui_buttons_list:
                button.get_state()
            if ui_storage.UIOptions.submenu_game_visible is True:
                for button in self.ui_submenu_game_button_list:
                    button.get_state()
            if ui_storage.UIOptions.submenu_display_visible is True:
                for button in self.ui_submenu_display_button_list:
                    button.get_state()
            if ui_storage.UIOptions.submenu_sound_visible is True:
                for button in self.ui_submenu_sound_button_list:
                    button.get_state()

        # EXECUTING BUTTONS STATES
        if ui_storage.UIOptions.input_control is True:
            for button in self.ui_buttons_list:
                button.do_action()
            if ui_storage.UIOptions.submenu_game_visible is True:
                for button in self.ui_submenu_game_button_list:
                    button.do_action()
            if ui_storage.UIOptions.submenu_display_visible is True:
                for button in self.ui_submenu_display_button_list:
                    button.do_action()
            if ui_storage.UIOptions.submenu_sound_visible is True:
                for button in self.ui_submenu_sound_button_list:
                    button.do_action()

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
                import storage as st
                st.Events.game.append('EVENT:ui_options:change_screen_game')
                print "change submenu to game"

    class UIButtonDisplay(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonDisplay, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False
                import storage as st
                st.Events.game.append('EVENT:ui_options:change_screen_display')
                print "change submenu to display"

    class UIButtonSound(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonSound, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False
                import storage as st
                st.Events.game.append('EVENT:ui_options:change_screen_sound')
                print "change submenu to sound"

    class UIButtonBack(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonBack, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self):
            import storage as st
            if self.last_pressed is True:
                print "back"
                st.Events.game.append('EVENT:ui_options:options_off')
                self.last_pressed = False

    class UIButtonDisplaySetMode(Button):
        def __init__(self, name):
            super(MenuOptions.UIButtonDisplaySetMode, self).__init__(name, hover=True)
            self.visible = False
            self.is_state_on = False

        def do_action(self):
            if self.last_pressed is True:
                self.last_pressed = False
                import storage as st
                st.Events.system.append('EVENT:ui_options:display:fullscreen_switch')

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