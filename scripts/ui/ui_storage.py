__author__ = 'Perkel'
from scripts.utils.load_graphic_sound import Button
import os


class UISettings:
    input_control = "main_menu"


class UIMainMenu:
    #GENERAL
    visible = True
    input_control = True

    transparency = object
    background = object
    ui_background = object
    who_made_this = object
    patreon = object

    button_continue = object
    button_new_game = object
    button_save = object
    button_load = object
    button_options = object
    button_quit = object

    # LISTS

    menu_background_list = list
    menu_button_list = list

    menu_background_visible_list = list
    menu_buttons_visible_list = list

    #POSITIONING MENU
    position = (100, 50)
    position_buttons = (position[0]+25, position[1]+40)
    buttons_y_difference = 75
    #BACKGROUND SCROLLING
    bck_scrolling_direction = 1
    bck_scrolling_speed = 50

    # IMAGES
    image_background = 'panorama.jpg'
    image_ui_background = 'mainmenubackground.png'
    image_transparency = 'menu_transparency.png'

    image_button_continue = 'main_menu_continue.png'
    image_button_new_game = 'main_menu_new_game.png'
    image_button_save     = 'main_menu_save.png'
    image_button_load     = 'main_menu_load.png'
    image_button_options  = 'main_menu_options.png'
    image_button_quit     = 'main_menu_quit.png'


class UIOptions:
    #GENERAL
    visible = False
    input_control = False

    submenu_game_visible = True
    submenu_display_visible = False
    submenu_sound_visible = False
    submenu_list = []

    # BUTTONS
    #main
    button_game = object
    button_display = object
    button_sound = object
    button_back = object
    #ui game
    #ui display
    button_display_mode = object
    #ui sound
    ui_sub_display_fullscreen = False

    #POSITIONING
    position = (50, 50)
    position_buttons = (position[0]+30, position[1]+40)
    buttons_y_difference = 75
    position_submenu = (position[0]+275, position[1]+40)
    #BUTTONS POSITION
    position_submenu_button_display_mode = (position_submenu[0]+400, position_submenu[1]+30)

    #IMAGES / background
    image_ui_transparency = 'menu_transparency.png'
    image_ui_main_background = 'options_menu_background.png'
    #       / options body backgrounds
    image_ui_game_background = 'body_game.png'
    image_ui_display_background = 'body_display.png'
    image_ui_sound_background = 'body_sound.png'
    #       / main buttons
    image_button_game = 'button_game.png'
    image_button_display = 'button_display.png'
    image_button_sound = 'button_sound.png'
    image_button_back = 'button_back.png'
    #       / buttons in display option
    image_button_switch_off = 'button_state_off.png'
    image_button_switch_on = 'button_state_on.png'


class UIPlayerCreation:
    #GENERAL
    visible = False
    input_control = False

    # BUTTONS
    button_back = object
    button_finish = object
    button_next_face = object
    button_previous_face = object
    button_next_background = object
    button_previooous_background = object

    #IMAGES      /   background
    image_background = "player_creation_screen.png"
    #            /   portraits
    image_face = "player-001.png"
    image_face_background = "player_background_001.png"
    #            /   buttons
    image_button_arrow_right = "pc_right_arrow.png"
    image_button_arrow_left = "pc_left_arrow.png"
    image_button_finish = "pc_button_finish.png"
    image_button_back = "pc_button_back.png"

    # counters for faces and faces backgrounds
    face_count = 0
    face_background_count = 0

    # listing faces and faces backgrounds
    path_faces = "data/art/player/head"
    path_faces_backgrounds = "data/art/player/backgrounds"

    list_faces = os.listdir(path_faces)
    list_background = os.listdir(path_faces_backgrounds)

    #POSITIONING

    #background
    position_background = (0, 0)
    #down bar
    position_bar_down = (0, 600)
    #portrait position
    portrait_position = (450, 100)
    player_portrait_position = (portrait_position[0]+100, portrait_position[1]+30)
    #buttons position
    position_button_finish = (position_bar_down[0]+912, position_bar_down[1]-5)
    position_button_back = (position_bar_down[0]+312, position_bar_down[1]-5)
    position_button_next_face = (
        portrait_position[0]+210,
        portrait_position[1]+30)
    position_button_next_face_background = (
        position_button_next_face[0],
        position_button_next_face[1]+60)
    position_button_previous_face = (
        position_button_next_face[0]-159,
        position_button_next_face[1])
    position_button_previous_face_background = (
        position_button_previous_face[0],
        position_button_next_face_background[1])


class UIGameplayMain():
    # GENERAL
    visible = False
    input_control = False

    # BUTTONS
    button_end_turn = object
    button_options = object
    button_quit_to_main_menu = object
    button_character_sheet = object
    button_finances = object
    button_current_date = object

    home = object
    downtown = object
    slums = object

    # IMAGES

    player_face = object
    player_face_background = object

    ui_money_background = object
    ui_house_background = object
    ui_lower_bar_ui = object
    ui_turn_background = object

    # NAMES OF FILES

    image_money_background = ''
    image_lower_bar_ui = ''
    image_turn_background = ''
    image_house_background = 'house_background_forest.jpg'

    # POSITIONING

    position_house_background = (0, 0)
    position_left_bar = (0, 0)
    position_down_bar = (0, 650)
    position_right_bar = (1150, 0)

    position_button_end_turn = (position_right_bar[0], position_right_bar[1]+5)
    position_face = (position_left_bar[0]+10, position_left_bar[1]+10)

    # LISTS

    list_city_background = list
    list_buttons = list
