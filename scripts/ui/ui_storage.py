__author__ = 'Perkel'
from scripts.utils.load_graphic_sound import Button


class UIMainMenu:
    #GENERAL
    visible = True
    input_control = True

    #POSITIONING
    position = (50, 50)
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


class UIPlayerCreation:
    #GENERAL
    visible = False
    input_control = False
    #POSITIONING
    # down bar
    position_bar_down = (0, 600)
    # portrait position
    portrait_position = (450, 100)
    player_portrait_position = (portrait_position[0]+100, portrait_position[1]+30)