import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from datetime import datetime

# Importation du fichier KV
kv_file = os.path.abspath("./Screen/main.kv")

# Définition des écrans
class MenuPrincipal(Screen):
    pass

class ListeDest(Screen):
    pass

class ListeVols(Screen):
    pass

class Application(App):
    def build(self):
        Builder.load_file(kv_file)

        """
        # Afficher les classes des widgets créés à partir du fichier KV

        root = MenuPrincipal()

        for widget in root.walk():
            print(type(widget))
        """
        # Définition du Screen Manager et ajout des écrans
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name='menu'))
        sm.add_widget(ListeDest(name='dest'))
        sm.add_widget(ListeVols(name='vols'))
        
        return sm
    
if __name__== '__main__':
    Application().run()