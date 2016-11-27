__author__ = 'Perkel'

from scripts.utils.load_graphic_sound import Button

#                                               OBJECTS
house_background = object
house = object
shed = object
farm = object

#                                               SWITCHES
switch_house = False
switch_house_background = True

#                                               IMAGES FILES
# background
image_name_house_background_forested = 'house_background_forest.jpg'
image_name_house_background_clear_half = str
image_name_house_background_clear_full = 'house_background_clear2.jpg'
# house
image_name_house_poor = 'house_poor1.png'
# shed
image_name_shed_poor = str
# farm
image_name_farm_poor = str


class ButtonHouse(Button):
        def __init__(self, name):
            import scripts.ui.ui_storage as ui_storage
            super(ButtonHouse, self).__init__(name, hover=True)
            self.description = "House"
            self.visible = True

        def do_action(self):
            if self.last_pressed is True:
                import storage as st
                self.last_pressed = False
                print self.description
                pass