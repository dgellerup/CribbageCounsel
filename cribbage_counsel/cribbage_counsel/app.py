
import toga
from toga.style import Pack
from toga.style.pack import *

from cribbage_counsel.CribbageCounsel import *

class CribbageCounsel(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        self.c_box = toga.Box(style=Pack(background_color='green', padding_top=30))
        self.c_input = toga.TextInput(style=Pack(width=200))
        c_label = toga.Label('Your hand', style=Pack(text_align=LEFT, width=70, background_color='green', padding_left=30))
        self.crib_check = toga.Switch('Your crib', style=Pack(text_align=CENTER, background_color='green', padding_left=20))

        self.rec_box = toga.Box(style=Pack(background_color='green'))
        self.rec_box.style.padding = 40
        self.rec_box.style.update(alignment=CENTER)
        self.rec_box.style.update(direction=ROW)

        # best_cards = ['4-d', '5-d', '6-d', '10-d']
        #
        # for card in best_cards:
        #     print(card)
        #     image = toga.Image(f'../resources/{card.replace("-", "")}.png')
        #     imageview = toga.ImageView(image)
        #     imageview.style.update(height=120)
        #     imageview.style.update(width=90)
        #     rec_box.add(imageview)

        button = toga.Button('Calculate', on_press=self.calculate, style=Pack(padding_left=20))

        self.c_box.add(c_label)
        self.c_box.add(self.c_input)
        self.c_box.add(self.crib_check)
        self.c_box.add(button)

        self.main_box = toga.Box(
            children=[self.c_box, self.rec_box],
            style=Pack(direction=COLUMN, background_color='green')
        )

        # Add the content on the main window
        self.main_window.content = self.main_box

        # Show the main window
        self.main_window.show()

    def calculate(self, widget):
        crib = True if self.crib_check.is_on else False
        best_cards = calc(str(self.c_input.value), crib)

        for card in best_cards:
            print(card)
            image = toga.Image(f'../resources/{card.replace("-", "")}.png')
            imageview = toga.ImageView(image)
            imageview.style.update(height=120)
            imageview.style.update(width=90)
            self.rec_box.add(imageview)

        self.rec_box.refresh()
        self.main_box.refresh()



def main():
    return CribbageCounsel('Cribbage Counsel', 'com.dgellerup.cribbage_counsel.cribbage_counsel')
