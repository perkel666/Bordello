__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuCharacterCreation():
    def __init__(self):

        """
        Creates Character Creatiion UI after you click New Game in Main Menu.

        Buttons actions are handled by EVENT:game in update_state.py while customization
        of buttons and graphics inside this ui is handled in ui_storage.py
        """
        import scripts.ui.ui_storage as ui_storage

        # UI INITIALIZATION
        self.face_confirm_count = 0
        self.face_background_confirm_count = 0

        self.menu_background_visible_list = []
        self.menu_buttons_visible_list = []
        self.player_portrait_front = []
        self.player_portrait_background = []

        # CREATION IMAGES/BUTTONS

        self.ui_background = \
            MenuCharacterCreation.MenuBackground(
                ui_storage.UIPlayerCreation.image_background)

        self.current_face = \
            MenuCharacterCreation.ButtonCurrentFace(
                ui_storage.UIPlayerCreation.image_face)

        self.current_face_background = \
            MenuCharacterCreation.ButtonCurrentFaceBackground(
                ui_storage.UIPlayerCreation.image_face_background)

        self.button_finish = MenuCharacterCreation.ButtonFinish(
            ui_storage.UIPlayerCreation.image_button_finish)

        self.button_next_face = \
            MenuCharacterCreation.ButtonNextFace(
                ui_storage.UIPlayerCreation.image_button_arrow_right)

        self.button_previous_face = \
            MenuCharacterCreation.ButtonPreviousFace(
                ui_storage.UIPlayerCreation.image_button_arrow_left)

        self.button_next_face_background = \
            MenuCharacterCreation.ButtonNextFaceBackground(
                ui_storage.UIPlayerCreation.image_button_arrow_right)

        self.button_previous_face_background = \
            MenuCharacterCreation.ButtonPreviousFaceBackground(
                ui_storage.UIPlayerCreation.image_button_arrow_left)

        # LISTS FOR DRAWING OM SCREEM
        # menu background list
        self.menu_background_list = [
            self.ui_background]

        # button list
        self.menu_button_list = [
            self.button_finish,
            self.button_next_face,
            self.button_previous_face,
            self.button_next_face_background,
            self.button_previous_face_background
        ]

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        if ui_storage.UIPlayerCreation.visible is True:
            self.menu_background_visible_list = []
            self.menu_buttons_visible_list = []
            self.player_portrait_front = [self.current_face]
            self.player_portrait_background = [self.current_face_background]

            # CHECK IF FACE CHANGED

            if self.face_background_confirm_count != ui_storage.UIPlayerCreation.face_background_count:
                self.face_background_confirm_count = ui_storage.UIPlayerCreation.face_background_count

                self.current_face_background = MenuCharacterCreation.ButtonCurrentFaceBackground(
                    ui_storage.UIPlayerCreation.list_background[ui_storage.UIPlayerCreation.face_background_count])

            # CHECK IF FACE BACKGROUND CHANGED

            if self.face_confirm_count != ui_storage.UIPlayerCreation.face_count:
                self.face_confirm_count = ui_storage.UIPlayerCreation.face_count

                self.current_face = MenuCharacterCreation.ButtonCurrentFace(
                    ui_storage.UIPlayerCreation.list_faces[ui_storage.UIPlayerCreation.face_count])

            # CREATING VISIBLE BUTTONS LIST
            for button in self.menu_button_list:
                if button.visible is True:
                    self.menu_buttons_visible_list.append(button)

            # CREATING VISIBLE BACKGROUND LIST
            for background in self.menu_background_list:
                if background.visible is True:
                    self.menu_background_visible_list.append(background)

            # POSITIONING

            # background image
            self.ui_background.rect = ui_storage.UIPlayerCreation.position_background
            # face and face backgroud
            self.current_face.rect = ui_storage.UIPlayerCreation.player_portrait_position
            self.current_face_background.rect = ui_storage.UIPlayerCreation.player_portrait_position
            # finish button
            self.button_finish.rect.x = \
                ui_storage.UIPlayerCreation.position_button_finish[0]
            self.button_finish.rect.y = \
                ui_storage.UIPlayerCreation.position_button_finish[1]
            # next face button
            self.button_next_face.rect.x = \
                ui_storage.UIPlayerCreation.position_button_next_face[0]
            self.button_next_face.rect.y = \
                ui_storage.UIPlayerCreation.position_button_next_face[1]
            # next face background button
            self.button_next_face_background.rect.x = \
                ui_storage.UIPlayerCreation.position_button_next_face_background[0]
            self.button_next_face_background.rect.y = \
                ui_storage.UIPlayerCreation.position_button_next_face_background[1]
            # previous face button
            self.button_previous_face.rect.x = \
                ui_storage.UIPlayerCreation.position_button_previous_face[0]
            self.button_previous_face.rect.y = \
                ui_storage.UIPlayerCreation.position_button_previous_face[1]
            # previous face background button
            self.button_previous_face_background.rect.x = \
                ui_storage.UIPlayerCreation.position_button_previous_face_background[0]
            self.button_previous_face_background.rect.y = \
                ui_storage.UIPlayerCreation.position_button_previous_face_background[1]

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
            layer_face_background.draw(st.Display.screen)
            layer_face.draw(st.Display.screen)
            layer_buttons.draw(st.Display.screen)

    def execute_actions(self):
        import scripts.ui.ui_storage as ui_storage
        # GETTING BUTTONS STATE IF IT/THEY WERE PRESSED
        if ui_storage.UIPlayerCreation.input_control is True:
            for button in self.menu_buttons_visible_list:
                button.get_state()

        # EXECUTING BUTTON IF IT WAS PRESSED
        if ui_storage.UIPlayerCreation.input_control is True:
            for button in self.menu_buttons_visible_list:
                button.do_action()

    #   BACKGROUND IMAGE

    class MenuBackground(Button):
        def __init__(self, name):
            super(MenuCharacterCreation.MenuBackground, self).__init__(name)
            self.description = "Background image"

    #   BUTTONS

    class ButtonFinish(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonFinish, self).__init__(name, hover=True)
            self.description = "Finish"

        def do_action(self):
            if self.last_pressed is True:
                print self.description
                self.last_pressed = False

    class ButtonNextFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonNextFace, self).__init__(name, hover=True, pressed=True)
            self.description = "Next Face"

        def do_action(self):
            if self.last_pressed is True:
                import storage as st
                print self.description
                self.last_pressed = False
                st.Events.game.append('EVENT:char_creator:next_face')

    class ButtonPreviousFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonPreviousFace, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous Face"

        def do_action(self):
            if self.last_pressed is True:
                import storage as st
                print self.description
                self.last_pressed = False
                st.Events.game.append('EVENT:char_creator:previous_face')

    class ButtonNextFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonNextFaceBackground, self).__init__(name, hover=True, pressed = True)
            self.description = "Next Face Background"

        def do_action(self):
            if self.last_pressed is True:
                import storage as st
                print self.description
                self.last_pressed = False
                st.Events.game.append('EVENT:char_creator:next_face_background')

    class ButtonPreviousFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonPreviousFaceBackground, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous Face Background"

        def do_action(self):
            if self.last_pressed is True:
                import storage as st
                print self.description
                self.last_pressed = False
                st.Events.game.append('EVENT:char_creator:previous_face_background')

    #    FACE IMAGES AND FACE BACKGROUND IMAGES

    class ButtonCurrentFace(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonCurrentFace, self).__init__(name)
            self.description = "Previous Face Background"

    class ButtonCurrentFaceBackground(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(MenuCharacterCreation.ButtonCurrentFaceBackground, self).__init__(name)
            self.description = "Previous Face Background"