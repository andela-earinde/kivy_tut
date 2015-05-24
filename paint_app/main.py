from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.base import EventLoop
from kivy.graphics import Color, Line
from kivy.utils import get_color_from_hex
from kivy.config import Config

class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return 
        with self.canvas:
            Color(*get_color_from_hex('#0080FF80'))
            Line(circle=(touch.x, touch.y, 25), width=4)

class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        if EventLoop.window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse
                a, b = pygame_compile_cursor()
                mouse.set_cursor((24, 24), (9, 9), a, b)
            except:
                pass

        return CanvasWidget()


if __name__ == "__main__":
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    #Config.set('input', 'mouse', 'mouse,disable_multitouch')

    from kivy.core.window import Window

    Window.clearcolor = get_color_from_hex('#ffffff')
    PaintApp().run()