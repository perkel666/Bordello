__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuGameplay():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage

        ui_storage.UIGameplayMain.ui_house_background = Button(ui_storage.UIGameplayMain.image_house_background)

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import scripts.gameplay.player as player
        import storage as st

        if ui_storage.UIGameplayMain.visible is True:
            ui_storage.UIGameplayMain.ui_house_background.rect = ui_storage.UIGameplayMain.position_city_background
            player.face.rect = ui_storage.UIGameplayMain.position_face
            player.face_background.rect = ui_storage.UIGameplayMain.position_face

    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        import scripts.gameplay.player as player
        if ui_storage.UIGameplayMain.visible is True:

            # CREATING SPRITE GROUPS

            layer_house_background = pg.sprite.Group()
            layer_city_objects = pg.sprite.Group()
            layer_city_weather_effects = pg.sprite.Group()
            layer_left_bar = pg.sprite.Group()
            layer_right_bar = pg.sprite.Group()
            layer_down_bar = pg.sprite.Group()
            layer_face_background = pg.sprite.Group()
            layer_face = pg.sprite.Group()
            layer_buttons = pg.sprite.Group()

            # ADDING SPRITES TO SPRITE GROUP

            layer_house_background.add(ui_storage.UIGameplayMain.ui_house_background)

            layer_face_background.add(player.face_background)
            layer_face.add(player.face)

            # DRAWING

            layer_house_background.draw(storage.Display.screen)
            layer_face_background.draw(storage.Display.screen)
            layer_face.draw(storage.Display.screen)

    def execute_actions(self):
        pass