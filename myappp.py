from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

Window.size = (500, 200)
Window.clearcolor = (255/255, 186/255, 2/255, 1)      # R\G\B
Window.title = "Kolini Veshchi"
class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='World Without WallS')

    def btn_pressed(self, *args):
        self.label.color = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)

    def build(self):
        box = BoxLayout()
        btn = Button(text='Touch Me')
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)
        return box


app = MyApp()
app.run()