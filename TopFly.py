from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from datetime import datetime

class ClockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        # Ajouter la barre de tâche en haut
        self.toolbar = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))
        self.home_button = Button(text="Home", size_hint=(0.2, 1))
        self.toolbar.add_widget(self.home_button)
        self.layout.add_widget(self.toolbar)

        # Ajouter les autres widgets (horloge, bouton Start)
        self.label = Label(text="Bonjour", font_size=30, size_hint=(1, 0.2),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.clock = Label(text="", font_size=30, size_hint=(1, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.button = Button(text="Start", size_hint=(1, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.button.bind(on_press=self.update)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.clock)
        self.layout.add_widget(self.button)
        Clock.schedule_interval(self.display_time, 1)
        return self.layout


    def display_time(self, dt):
        self.clock.text = str(datetime.now().time())[:8]

    def update(self, instance):
        if self.button.text == "Start":
            self.start = datetime.now()
            self.button.text = "Stop"
        else:
            self.stop = datetime.now()
            self.button.text = "Start"
            self.duration = self.stop - self.start
            self.label.text = "Le vol a duré : " + str(self.duration)

if __name__ == "__main__":
    ClockApp().run()
