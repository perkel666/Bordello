__author__ = 'Perkel'


def render_main_menu_ui():
    import scripts.ui.ui_objects as ui_objects
    for menu in ui_objects.ui_main_list:
        menu.draw_menu()