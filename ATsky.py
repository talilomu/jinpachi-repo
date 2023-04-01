import os
import sqlite3
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.menu import MDDropdownMenu
from datetime import datetime

kv_file = os.path.abspath("./Screen/ATsky.kv")

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class KivyApp(MDApp):
    def build(self):    
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        choix_list = ["choix 1", "choix 2", "choix 3"]
        self.dt = []
        for choix in choix_list:
            self.dt.append({
                "viewclass": "OneLineListItem",
                "text": choix,
                "on_release": lambda x=choix: self.menu_callback(x)
                })
        Clock.schedule_interval(self.update_time, 1)  # Schedule update_time to be called every second
        return Builder.load_file(kv_file)

    def show_menu(self):
        caller=self.root.ids.drop_menu
        self.menu = MDDropdownMenu(
        caller=caller,
        items=self.dt,
        width_mult=4, 
        on_release=self.menu_callback
        )
        self.menu.open()

    def menu_callback(self, instance_menu_item):
        self.choix = instance_menu_item
        self.root.ids.drop_menu.text = "Selected destination: " + instance_menu_item
        self.menu.dismiss()
    
    def update_time(self, *args):
        # Update time_label with the current time
        self.root.ids.time_label.text = datetime.now().strftime('%H:%M:%S')

    def save_fly(self):
        if(self.root.ids.bouton.text == "Démarrer"):
            self.start = datetime.now()
            self.root.ids.bouton.text = "Stop"
        else:
            self.stop = datetime.now()
            self.root.ids.bouton.text = "Démarrer"
            self.duration = self.stop - self.start
            self.root.ids.duree.text = "Le vol " + self.choix + " a duré : " + str(self.duration)

KivyApp().run()