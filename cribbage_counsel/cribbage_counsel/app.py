
import toga
from toga.style import Pack
from toga.style.pack import *

from cribbage_counsel.CribbageCounsel import *

class CribbageCounsel(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        c_box = toga.Box(style=Pack(background_color='green', padding_top=30))
        c_input = toga.TextInput(style=Pack(width=200))
        c_label = toga.Label('Your hand', style=Pack(text_align=LEFT, width=70, background_color='green', padding_left=30))
        crib_check = toga.Switch('Your crib', style=Pack(text_align=CENTER, background_color='green', padding_left=20))

        rec_box = toga.Box(style=Pack(background_color='green'))
        rec_box.style.padding = 40
        rec_box.style.update(alignment=CENTER)
        rec_box.style.update(direction=ROW)

        def calculate(widget):
            best_cards = calc(str(c_input.value))

            for card in best_cards:
                print(card)
                image = toga.Image(f'../resources/{card.replace("-", "")}.png')
                imageview = toga.ImageView(image)
                imageview.style.update(height=120)
                imageview.style.update(width=90)
                rec_box.add(imageview)

        button = toga.Button('Calculate', on_press=calculate, style=Pack(padding_left=20))

        c_box.add(c_label)
        c_box.add(c_input)
        c_box.add(crib_check)
        c_box.add(button)

        main_box = toga.Box(
            children=[c_box, rec_box],
            style=Pack(direction=COLUMN, background_color='green')
        )

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return CribbageCounsel('Cribbage Counsel', 'com.dgellerup.cribbage_counsel.cribbage_counsel')
