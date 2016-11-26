__author__ = 'Perkel'

import pygame as pg
from scripts.utils.load_graphic_sound import Button


class MenuGameplay():
    def __init__(self):
        import scripts.ui.ui_storage as ui_storage

        ui_storage.UIGameplayMain.ui_city_background = Button(ui_storage.UIGameplayMain.image_city_background)

    def menu_logic(self):
        import scripts.ui.ui_storage as ui_storage
        import scripts.gameplay.player as player
        import storage as st

        if ui_storage.UIGameplayMain.visible is True:
            ui_storage.UIGameplayMain.ui_city_background.rect = ui_storage.UIGameplayMain.position_city_background
            ui_storage.UIGameplayMain.player_face.rect = ui_storage.UIGameplayMain.position_face
            ui_storage.UIGameplayMain.player_face_background.rect = ui_storage.UIGameplayMain.position_face

    def draw_menu(self):
        import scripts.ui.ui_storage as ui_storage
        import storage
        if ui_storage.UIGameplayMain.visible is True:

            # CREATING SPRITE GROUPS

            layer_city_background = pg.sprite.Group()
            layer_city_objects = pg.sprite.Group()
            layer_city_weather_effects = pg.sprite.Group()
            layer_left_bar = pg.sprite.Group()
            layer_right_bar = pg.sprite.Group()
            layer_down_bar = pg.sprite.Group()
            layer_face_background = pg.sprite.Group()
            layer_face = pg.sprite.Group()
            layer_buttons = pg.sprite.Group()

            # ADDING SPRITES TO SPRITE GROUP

            layer_city_background.add(ui_storage.UIGameplayMain.ui_city_background)
            layer_face_background.add(ui_storage.UIGameplayMain.player_face_background)
            layer_face.add(ui_storage.UIGameplayMain.player_face)

            # DRAWING

            layer_city_background.draw(storage.Display.screen)
            layer_face_background.draw(storage.Display.screen)
            layer_face.draw(storage.Display.screen)

    def execute_actions(self):
        pass