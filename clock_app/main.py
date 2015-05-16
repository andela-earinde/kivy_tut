from kivy.app import App
from kivy.core.text import LabelBase 
from time import strftime
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)

class ClockApp(App):
    
    def update_time(self, nap):
        self.root.time_prop.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    Window.clearcolor = get_color_from_hex('#101216')

    LabelBase.register(name="Roboto",
                       fn_regular="Roboto-Thin.ttf",
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
