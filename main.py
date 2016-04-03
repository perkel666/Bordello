from __future__ import division

__author__ = 'Perkel'

import pygame as pg
import scripts.user_input as user_input
import scripts.update_state as update_state

# loadResources()
# gamestate()
# initialization()


class Game(object):
    def __init__(self):
        import storage as st
        pg.init()
        # INITIALIZATION OF DEFAULT storage.py VALUES
        # !!!! Implement reading settings.ini !!!            <---------------
        # system
        st.System.clock = pg.time.Clock()
        st.System.isGameStillRunning = True
        # display
        st.Display.fullscreen = False
        st.Display.framerate = 120
        st.Display.screen = (1280, 720)
        # events
        st.Events.pygame = pg.event.get()
        st.Events.system = []

        # ININTIALIZATION OF DISPLAY
        pg.display.set_mode(st.Display.screen)

    def main_loop(self):
        import storage as st
        while st.System.isGameStillRunning is True:
            pg.display.update()
            self.start_frame()
            self.get_user_input()
            self.update_state()
            self.render_sound()
            self.render_screen()

    def start_frame(self):
        import storage as st
        st.System.clock.tick(st.Display.framerate)
        st.Events.pygame = pg.event.get()

    def get_user_input(self):
        user_input.mouse_input()
        user_input.keyboard_input()

    def update_state(self):
        update_state.keyboard_system_events()
        update_state.handle_system_events()

    def render_sound(self):
        pass

    def render_screen(self):
        #LAYERS
        #  Gameplay
        #  Gameplay UI
        #  Main Menu
        #DISPLAY EVERYTHING
        pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.main_loop()