__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuMain():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage

        self.menu_background_visible_list = []
        self.menu_buttons_visible_list = []

        #LOAD SPRITES from ui_storage.py
        # background
        self.background = MenuMain.MenuBackground(ui_storage.UIMainMenu.image_background)
        self.background_ui = MenuMain.MainMenuUI(
            ui_storage.UIMainMenu.image_ui_background,
            ui_storage.UIMainMenu.position)
        self.background_transparency = MenuMain.BackgroundTransparent(
            ui_storage.UIMainMenu.image_transparency
        )
        # buttons
        self.button_continue = MenuMain.ButtonContinue(ui_storage.UIMainMenu.image_button_continue)
        self.button_new_game = MenuMain.ButtonNewGame(ui_storage.UIMainMenu.image_button_new_game)
        self.button_save = MenuMain.ButtonSave(ui_storage.UIMainMenu.image_button_save)
        self.button_load = MenuMain.ButtonLoad(ui_storage.UIMainMenu.image_button_load)
        self.button_options = MenuMain.ButtonOptions(ui_storage.UIMainMenu.image_button_options)
        self.button_quit = MenuMain.ButtonsQuit(ui_storage.UIMainMenu.image_button_quit)

        # menu background list
        self.menu_background_list = self.menu_background_list = [
            self.background_transparency,
            self.background]
        # button list
        self.menu_button_list = [
            self.button_continue,
            self.button_new_game,
            self.button_save,
            self.button_load,
            self.button_options,
            self.button_quit]

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import storage as st

        if ui_storage.UIMainMenu.visible is True:
            # LOCALS
            self.menu_background_visible_list = []
            self.menu_buttons_visible_list = []

            # CREATING VISIBLE BUTTONS LIST
            for button in self.menu_button_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            # CREATING VISIBLE BACKGROUND LIST (depends on: if game.new_game_started is True or False)
            for background in self.menu_background_list:
                if background.visible is True:
                    self.menu_background_visible_list.append(background)

            # POSITIONING BUTTONS ON MAIN MENU
            difference = 0  # initial difference
            for button in self.menu_buttons_visible_list:
                button.rect.x = ui_storage.UIMainMenu.position_buttons[0]
                button.rect.y = ui_storage.UIMainMenu.position_buttons[1] + difference
                difference += ui_storage.UIMainMenu.buttons_y_difference

            if self.background.rect.x >= 0:
                ui_storage.UIMainMenu.bck_scrolling_direction = 1
            elif self.background.rect.x <= -880:
                ui_storage.UIMainMenu.bck_scrolling_direction = -1

            self.background.true_position_x -= (ui_storage.UIMainMenu.bck_scrolling_speed
                                                * st.System.dt_seconds
                                                * ui_storage.UIMainMenu.bck_scrolling_direction)
            self.background.rect.x = self.background.true_position_x

    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        if ui_storage.UIMainMenu.visible is True:

            layer_main_menu_buttons = pg.sprite.Group()
            layer_main_menu_background = pg.sprite.Group()
            layer_main_menu_ui_graphic = pg.sprite.Group()

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

    def execute_actions(self):
        # GETTING BUTTONS STATES
        import scripts.ui.ui_storage as ui_storage
        if ui_storage.UIMainMenu.input_control is True:
            for button in self.menu_buttons_visible_list:
                button.get_state()
        # EXECUTING BUTTON IF IT WAS PRESSED
        if ui_storage.UIMainMenu.input_control is True:
            for button in self.menu_buttons_visible_list:
                button.do_action()

    class BackgroundTransparent(Button):
        def __init__(self, name):
            super(MenuMain.BackgroundTransparent, self).__init__(name)
            self.description = "Background transparency"
            self.visible = False

    class MenuBackground(Button):
        def __init__(self, name):
            super(MenuMain.MenuBackground, self).__init__(name)
            self.description = "Background image"
            self.visible = True

    class MainMenuUI(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(MenuMain.MainMenuUI, self).__init__(name)
            self.description = "Main menu UI"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]
            self.visible = True

    # BUTTONS #########

    class ButtonContinue(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonContinue, self).__init__(name, hover=True)
            self.description = "Continue game"
            self.order = 1
            self.visible = False

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonNewGame(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonNewGame, self).__init__(name, hover=True)
            self.description = "New game"
            self.order = 2

        def do_action(self):
            import scripts.ui.ui_storage as ui_storage
            import storage as st
            if self.last_pressed is True:
                self.last_pressed = False
                import storage as st
                st.Events.game.append('EVENT:main_menu:start_new_game')

    class ButtonSave(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonSave, self).__init__(name, hover=True)
            self.description = "Save progress"
            self.order = 3

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonLoad(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonLoad, self).__init__(name, hover=True)
            self.description = "Load progress"
            self.order = 4

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonOptions(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonOptions, self).__init__(name, hover=True)
            self.description = "Configure options"
            self.order = 5

        def do_action(self):
            if self.last_pressed is True:
                import scripts.ui.ui_storage as ui_storage
                import storage as st
                self.last_pressed = False
                st.Events.game.append("EVENT:main_menu:options_on")

    class ButtonsQuit(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuMain.ButtonsQuit, self).__init__(name, hover=True)
            self.description = "Quit"
            self.order = 6

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False
                import storage as st
                st.Events.game.append('EVENT:main_menu:quit')


