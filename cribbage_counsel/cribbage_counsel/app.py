
import toga
from toga.style import Pack
from toga.style.pack import *


class CribbageCounsel(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        #main_box = toga.Box(style=Pack(background_color='green'))

        box = toga.Box(style=Pack(background_color='green'))
        box.style.padding = 40
        box.style.update(alignment=CENTER)
        box.style.update(direction=ROW)

        cards = ['2D', '3D', '4D', '5D', '6D']

        for card in cards:
            image = toga.Image(f'../resources/{card}.png')
            imageview = toga.ImageView(image)
            imageview.style.update(height=120)
            imageview.style.update(width=90)
            box.add(imageview)

        #main_box.add(box)

        # Add the content on the main window
        self.main_window.content = box

        # Show the main window
        self.main_window.show()


def main():
    return CribbageCounsel('Cribbage Counsel', 'com.dgellerup.cribbage_counsel.cribbage_counsel')
