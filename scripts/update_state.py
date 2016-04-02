__author__ = 'Perkel'
import pygame as pg

def keyboard_system_events():
    from main import storage

    for key in storage.keys_pressed:
        if key[pg.K_ESCAPE] is True:
            x = storage.events_game.append('QUIT')
            return x