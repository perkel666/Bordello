__author__ = 'Perkel'

class System:
    debug = bool
    isGameStillRunning = bool
    newGameStarted = bool
    clock = None
    dt = float
    dt_seconds = float


class Files:
    import scripts.utils.data_file_handling as f
    import scripts.ui.menu_main as ui
    #import
    files = f.FileList()


class Display:
    resolution = (1280, 720)
    framerate = int
    screen = object
    fullscreen = bool
    fullscreen_switch = bool


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