__author__ = 'Perkel'

import scripts.ui.menu_main as menu_main
import scripts.ui.menu_options as menu_options
import scripts.ui.menu_character_creation as char_creation

"""
This is file to create menu objects like main meny, options menu etc and put them into
a list which later there will be iteration upon

If you create new UI element it needs to go here. First it neds to be initialized as:
XXXXXX = new_menu.NewMenu()

then added to list which is used in update_state.py script
"""

ui_menu_main = menu_main.MenuMain()
ui_menu_options = menu_options.MenuOptions()
ui_menu_character_creation = char_creation.MenuCharacterCreation()

ui_main_list = [
    ui_menu_main,
    ui_menu_options,
    ui_menu_character_creation
]