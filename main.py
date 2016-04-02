from __future__ import division

__author__ = 'Perkel'

import pygame as pg
import scripts.user_input as user_input
import scripts.utils.data_file_handling as file_handling

# loadResources()

storage = file_handling.Storage()
# gamestate()
# initialization()


class Game(object):
    def __init__(self):
        self.running = True

        self.framerate = 120
        self.screen = (1280, 720)

        self.clock = pg.time.Clock()

        self.events_pygame = []
        self.events_game = []

        pg.init()
        pg.display.set_mode(self.screen)

    def main_loop(self):
        while self.running is True:
            pg.display.update()
            self.start_frame()
            self.get_user_input()
            self.update_state()
            #renderSound()
            self.render_screen()

    def start_frame(self):
        global storage
        self.clock.tick(self.framerate)
        self.events_pygame = pg.event.get()
        storage.events_pygame = self.events_pygame
        self.events_game = []

    def get_user_input(self):
        storage.mouse_pressed, storage.mouse_pos = user_input.mouse_input()
        storage.keys_pressed = user_input.keyboard_input()

    def update_state(self):
        for event in storage.events_game:
            if event == 'QUIT':
                self.running = False
                print "QUITING GAME"

    def render_sound(self):
        pass

    def render_screen(self):
        #Gameplay
        #Gameplay UI
        #Main Menu
        pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.main_loop()