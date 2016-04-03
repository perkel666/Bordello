__author__ = 'Perkel'

import scripts.ui.menu_main as menu_main
import scripts.ui.menu_options as menu_options

ui_menu_main = menu_main.MenuMain()
ui_menu_options = menu_options.MenuOptions()

ui_main_list = [
    ui_menu_main,
    ui_menu_options
]