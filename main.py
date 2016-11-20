from __future__ import division

__author__ = 'Perkel'

import pygame as pg
import scripts.user_input as user_input
import scripts.update_state as update_state


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
        st.Display.resolution = (1280, 720)
        st.Display.fullscreen = False
        st.Display.fullscreen_switch = st.Display.fullscreen
        st.Display.framerate = 50
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
            self.render_screen()
            self.render_sound()
            self.execute_state()

    def start_frame(self):
        import storage as st
        st.System.dt = st.System.clock.tick(st.Display.framerate)
        st.System.dt_seconds = st.System.dt / 1000
        st.Events.pygame = pg.event.get()
        st.Events.game = []
        st.Events.system = []

    def get_user_input(self):
        user_input.mouse_input()
        user_input.keyboard_input()

    def update_state(self):

        # input
        update_state.keyboard_system_events()
        # gameplay
        # gameplay ui
        # main menu ui
        update_state.ui_main_ui_logic()
        # system
        update_state.handle_system_events()

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

    def execute_state(self):
        update_state.ui_execute_ui_logic()
        update_state.handle_events_ui_game()

if __name__ == "__main__":
    game = Game()
    game.main_loop()