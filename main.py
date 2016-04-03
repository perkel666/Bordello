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
        st.System.debug = True
        st.System.clock = pg.time.Clock()
        st.System.isGameStillRunning = True
        st.System.newGameStarted = False
        # display
        st.Display.fullscreen = False
        st.Display.fullscreen_switch = st.Display.fullscreen
        st.Display.framerate = 120
        st.Display.screen = pg.display.set_mode(st.Display.resolution)
        # events
        st.Events.pygame = pg.event.get()
        st.Events.system = []

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
        st.System.dt = st.System.clock.tick(st.Display.framerate)
        st.System.dt_seconds = st.System.dt / 1000
        st.Events.pygame = pg.event.get()

    def get_user_input(self):
        user_input.mouse_input()
        user_input.keyboard_input()

    def update_state(self):
        update_state.keyboard_system_events()
        update_state.ui_main_ui_logic()
        update_state.handle_system_events()
        # gameplay
        # gameplay ui
        # main menu ui

    def render_sound(self):
        pass

    def render_screen(self):
        import scripts.render_screen as r
        #LAYERS
        #  Gameplay
        #  Gameplay UI
        #  Main Menu
        r.render_main_menu_ui()
        #DISPLAY EVERYTHING
        pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.main_loop()