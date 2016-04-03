__author__ = 'Perkel'


class System:
    isGameStillRunning = bool
    clock = None


class Display:
    framerate = int
    screen = tuple
    fullscreen = bool


class Player:
    health = int
    stamina = int


class Events:
    game = list
    system = list
    pygame = list


class Input:
    # ALL CURRENT INPUT
    all_input = list
    # MOUSE
    mouse_pos = tuple
    mouse_pressed_buttons = list
    mouse_movement = tuple
    # KEYBOARD
    keys_pressed = list
    # JOYSTICK