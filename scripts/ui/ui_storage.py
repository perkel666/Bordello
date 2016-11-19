__author__ = 'Perkel'
from scripts.utils.load_graphic_sound import Button
import os

class UISettings:
    input_control = "main_menu"

class UIMainMenu:
    #GENERAL
    visible = True
    input_control = True

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
    image_button_display_set_mode = 'button_state_off.png'


class UIPlayerCreation:
    #GENERAL
    visible = False
    input_control = False

    # listing faces and faces backgrounds
    path_faces = "data/art/player/head"
    path_faces_backgrounds = "data/art/player/backgrounds"

    list_faces = os.listdir(path_faces)
    list_background = os.listdir(path_faces_backgrounds)

    current_face = 0
    current_faces_background = 0

    #POSITIONING
    #background
    position_background = (0, 0)
    #down bar
    position_bar_down = (0, 600)
    #portrait position
    portrait_position = (450, 100)
    player_portrait_position = (portrait_position[0]+100, portrait_position[1]+30)
    #buttons position
    position_button_finish = (position_bar_down[0]+500, position_bar_down[1]+20)
    position_button_next_face = (
        portrait_position[0]+105,
        portrait_position[1]+80)
    position_button_previous_face = (
        position_button_next_face[0] - 150,
        position_button_next_face[1])
    position_button_next_face_background = (
        position_button_next_face[0],
        position_button_next_face[1]+50)
    position_button_previous_face_background = (
        position_button_previous_face[0],
        position_button_next_face_background[1])

    #IMAGES      /   background
    image_background = "player_creation_screen.jpg"
    #            /   portraits
    image_face = list_faces[current_face]
    image_face_background = list_background[current_faces_background]
    #            /   buttons
    image_button_arrow_right = "pc_right_arrow.png"
    image_button_arrow_left = "pc_left_arrow.png"
    image_button_finish = "pc_button_finish.png"
