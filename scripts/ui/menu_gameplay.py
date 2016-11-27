__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuGameplay():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage
        import scripts.gameplay.house as house

        # UI INIT

        ui_storage.UIGameplayMain.ui_face_background = Button(ui_storage.UIGameplayMain.image_face_background)

        # HOUSE AREA INIT
        house.house_background = Button(house.image_name_house_background_forested)
        house.house_background.rect = ui_storage.UIGameplayMain.position_house_background

        house.house = house.ButtonHouse(house.image_name_house_poor)
        house.house.rect.x = ui_storage.UIGameplayMain.position_house[0]
        house.house.rect.y = ui_storage.UIGameplayMain.position_house[1]

        self.buttons_list = []
        self.button_render = []

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import scripts.gameplay.player as player
        import scripts.gameplay.house as house
        import storage as st

        if ui_storage.UIGameplayMain.visible is True:

            self.buttons_list = [
                house.house
            ]

            # HOUSE BACKGROUND IMAGE STATE
            if house.switch_house_background is True:
                if player.house_background == 0:
                    house.house_background = Button(house.image_name_house_background_forested)
                    house.house_background.rect = ui_storage.UIGameplayMain.position_house_background
                    house.switch_house_background = False
                elif player.house_background == 1:
                    house.house_background = Button(house.image_name_house_background_forested)
                    house.house_background.rect = ui_storage.UIGameplayMain.position_house_background
                    house.switch_house_background = False
                elif player.house_background == 2:
                    house.house_background = Button(house.image_name_house_background_clear_full)
                    house.house_background.rect = ui_storage.UIGameplayMain.position_house_background
                    house.switch_house_background = False

            # HOUSE
            if house.switch_house is True:
                if player.house == 0:
                    house.house = Button(house.image_name_house_poor)
                    house.house.rect = ui_storage.UIGameplayMain.position_house
                    house.switch_house = False
            # SHED
            # FARM
            # PLAYER FACE
            player.face.rect = ui_storage.UIGameplayMain.position_face
            player.face_background.rect = ui_storage.UIGameplayMain.position_face

            ui_storage.UIGameplayMain.ui_face_background.rect = ui_storage.UIGameplayMain.position_left_bar

            # buttons list

            for button in self.buttons_list:
                if button.visible is True:
                    self.button_render.append(button)


    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        import scripts.gameplay.player as player
        import scripts.gameplay.house as house
        if ui_storage.UIGameplayMain.visible is True:

            # CREATING SPRITE GROUPS

            layer_house_background = pg.sprite.Group()
            layer_house_objects = pg.sprite.Group()
            layer_house_weather_effects = pg.sprite.Group()
            layer_left_bar = pg.sprite.Group()
            layer_right_bar = pg.sprite.Group()
            layer_down_bar = pg.sprite.Group()
            layer_face_background = pg.sprite.Group()
            layer_face = pg.sprite.Group()
            layer_buttons = pg.sprite.Group()

            # ADDING SPRITES TO SPRITE GROUP

            layer_house_background.add(house.house_background)
            #layer_house_objects.add(house.house)
            for button in self.button_render:
                layer_house_objects.add(button)
            layer_left_bar.add(ui_storage.UIGameplayMain.ui_face_background)

            layer_face_background.add(player.face_background)
            layer_face.add(player.face)

            # DRAWING

            layer_house_background.draw(storage.Display.screen)
            layer_house_objects.draw(storage.Display.screen)
            layer_left_bar.draw(storage.Display.screen)
            layer_face_background.draw(storage.Display.screen)
            layer_face.draw(storage.Display.screen)

    def execute_actions(self):
        import scripts.ui.ui_storage as ui_storage
        import scripts.gameplay.house as house
        # GETTING BUTTONS STATE IF IT/THEY WERE PRESSED
        if ui_storage.UIGameplayMain.input_control is True:
            for button in self.buttons_list:
                button.get_state()

        # EXECUTING BUTTON IF IT WAS PRESSED
        if ui_storage.UIGameplayMain.input_control is True:
            for button in self.buttons_list:
                pass