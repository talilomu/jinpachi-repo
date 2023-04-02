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

kv_file = os.path.abspath("./Screen/ATfly.kv")

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class KivyApp(MDApp):

    # Create database and tables
    conn = sqlite3.connect('./Data/airtahiti.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Vol
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  depart TEXT,
                  arrivee TEXT,
                  duree TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Destination
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom TEXT)''')
    
    conn.commit()
    conn.close()

    dest_list = ["Tahiti", "Bora Bora", "Rangiroa"]

    def build(self):
        self.dt1 = [] 
        self.dt2 = []
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"

        for choix in self.dest_list:
            self.dt1.append({
                "viewclass": "OneLineListItem",
                "text": choix,
                "on_release": lambda x=choix: self.menu1_callback(x)
                })
            
            self.dt2.append({
                "viewclass": "OneLineListItem",
                "text": choix,
                "on_release": lambda x=choix: self.menu2_callback(x)
                })
            
        Clock.schedule_interval(self.update_time, 1)  # Schedule update_time to be called every second
        return Builder.load_file(kv_file)

    def show_menu1(self):
        caller=self.root.ids.depart
        self.menu = MDDropdownMenu(
        caller=caller,
        items=self.dt1,
        width_mult=4, 
        on_release=self.menu1_callback
        )
        self.menu.open()

    def show_menu2(self):
        caller=self.root.ids.arrive
        self.menu = MDDropdownMenu(
        caller=caller,
        items=self.dt2,
        width_mult=4, 
        on_release=self.menu2_callback
        )
        self.menu.open()

    def menu1_callback(self, instance_menu_item):
        self.choix1 = instance_menu_item
        self.root.ids.depart.text = "Départ : " + instance_menu_item
        self.menu.dismiss()

    def menu2_callback(self, instance_menu_item):
        self.choix2 = instance_menu_item
        self.root.ids.arrive.text = "Arrivée : " + instance_menu_item
        self.menu.dismiss()
    
    def update_time(self, *args):
        # Update time_label with the current time
        self.root.ids.time_label.text = datetime.now().strftime('%H:%M:%S')

    def save_fly(self):
        try:
            if(self.root.ids.bouton.text == "Démarrer"):
                self.start = datetime.now()
                self.root.ids.bouton.text = "Stop"
            else:
                self.stop = datetime.now()
                self.root.ids.bouton.text = "Démarrer"
                self.duration = self.stop - self.start
                sec = self.duration.seconds
                self.duration = sec.strftime('%H:%M:%S')
                self.root.ids.duree.text = "Le vol " + self.choix1 + " - " + self.choix2 + " a duré : " + str(self.duration)

            self.root.ids.list_vol.text = self.choix1 + " " + self.choix2 + "\n"
        except EOFError as er:
            print(er)
            self.root.ids.duree.text = "Veuillez sélectionner une destination !"

KivyApp().run()