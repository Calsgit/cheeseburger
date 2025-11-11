from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class kivything(App):
    def build(self):
        """Build the kivy application."""
        self.title = "cheeseburger"
        self.root = Builder.load_file('layout.kv')
        return self.root