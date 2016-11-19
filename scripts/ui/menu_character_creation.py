__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuCharacterCreation():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage

        # UI INITIALIZATION

        self.menu_background_visible_list = []
        self.menu_buttons_visible_list = []
        self.player_portrait_front = []
        self.player_portrait_background = []

        # background
        self.ui_background = MenuCharacterCreation.MenuBackground(ui_storage.UIPlayerCreation.image_background)

        # menu background list
        self.menu_background_list = [
            self.ui_background]

        # creating buttons
        self.button_finish = MenuCharacterCreation.ButtonFinish(
            ui_storage.UIPlayerCreation.image_button_finish)
        self.button_next_face = MenuCharacterCreation.ButtonNextFace(
            ui_storage.UIPlayerCreation.image_button_arrow_right
        )
        self.button_previous_face = MenuCharacterCreation.ButtonPreviousFace(
            ui_storage.UIPlayerCreation.image_button_arrow_left
        )
        self.button_next_face_background = MenuCharacterCreation.ButtonNextFaceBackground(
            ui_storage.UIPlayerCreation.image_button_arrow_right
        )
        self.button_previous_face_background = MenuCharacterCreation.ButtonPreviousFaceBackground(
            ui_storage.UIPlayerCreation.image_button_arrow_left
        )

        self.current_face = ui_storage.UIPlayerCreation.list_faces[
            ui_storage.UIPlayerCreation.current_face]
        self.current_face_background = ui_storage.UIPlayerCreation.list_background[
            ui_storage.UIPlayerCreation.current_faces_background
        ]
        # button list
        self.menu_button_list = [
            self.current_face,
            self.current_face_background,
            self.button_next_face,
            self.button_previous_face,
            self.button_next_face_background,
            self.button_previous_face_background,
            self.button_finish
        ]

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage

        if ui_storage.UIPlayerCreation.visible is True:
            # LOCALS
            self.menu_background_visible_list = []
            self.menu_buttons_visible_list = []
            self.player_portrait_front = [self.current_face]
            self.player_portrait_background = [self.current_face_background]

            # CREATING VISIBLE BUTTONS LIST
            for button in self.menu_button_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            # CREATING VISIBLE BACKGROUND LIST
            for background in self.menu_background_list:
                if background.visible is True:
                    self.menu_background_visible_list.append(background)

            # POSITIONING

            self.ui_background.rect = ui_storage.UIPlayerCreation.position_background

            self.current_face.rect = ui_storage.UIPlayerCreation.player_portrait_position
            self.current_face_background.rect = ui_storage.UIPlayerCreation.player_portrait_position

            self.button_finish.rect = ui_storage.UIPlayerCreation.position_button_finish
            self.button_next_face = ui_storage.UIPlayerCreation.position_button_next_face
            self.button_previous_face = ui_storage.UIPlayerCreation.position_button_previous_face
            self.button_next_face_background = ui_storage.UIPlayerCreation.position_button_next_face_background
            self.button_previous_face_background = ui_storage.UIPlayerCreation.position_button_previous_face_background

            # GETTING BUTTONS STATE IF IT/THEY WERE PRESSED
            if ui_storage.UIPlayerCreation.input_control is True:
                for button in self.menu_buttons_visible_list:
                    button.get_state()

            # EXECUTING BUTTON IF IT WAS PRESSED
            if ui_storage.UIPlayerCreation.input_control is True:
                for button in self.menu_buttons_visible_list:
                    button.do_action()

    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage as st
        if ui_storage.UIPlayerCreation.visible is True:

            layer_buttons = pg.sprite.Group()
            layer_background = pg.sprite.Group()
            layer_face = pg.sprite.Group(self.player_portrait_front)
            layer_face_background = pg.sprite.Group(self.player_portrait_background)

            # ADD SPRITES TO LAYERS

            for button in self.menu_buttons_visible_list:
                layer_buttons.add(button)
            for background in self.menu_background_visible_list:
                layer_background.add(background)

            # DISPLAY LAYERS
            layer_background.draw(st.Display.screen)
            layer_face_background(st.Display.screen)
            layer_face.draw(st.Display.screen)
            layer_buttons.draw(st.Display.screen)

    class MenuBackground(Button):
        def __init__(self, name):
            super(MenuCharacterCreation.MenuBackground, self).__init__(name)
            self.description = "Background image"
            self.visible = True

    class ButtonFinish(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonFinish, self).__init__(name, hover=True)
            self.description = "Finish"
            self.order = 1

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonNextFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonNextFace, self).__init__(name, hover=True)
            self.description = "Next Face"
            self.order = 2

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonPreviousFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonPreviousFace, self).__init__(name, hover=True)
            self.description = "Previous Face"
            self.order = 3

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonNextFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonNextFaceBackground, self).__init__(name, hover=True)
            self.description = "Next Face Background"
            self.order = 4

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonPreviousFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonPreviousFaceBackground, self).__init__(name, hover=True)
            self.description = "Previous Face Background"
            self.order = 5

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonCurrentFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonCurrentFace, self).__init__(name)
            self.description = "Previous Face Background"
            self.order = 10

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonCurrentFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonCurrentFaceBackground, self).__init__(name)
            self.description = "Previous Face Background"
            self.order = 11

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False