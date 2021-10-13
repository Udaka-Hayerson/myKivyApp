from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button

from random import randint

Window.size = (250, 200)
Window.clearcolor = (210/255, 142/255, 70/255, 1)      # R\G\B
Window.title = "Kolini Veshchi(convector)"

class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='World Without WallS')
        self.miles = Label(text='Miles')
        self.metres = Label(text='Metres')
        self.santimetres = Label(text='Santimetres')
        self.input_data = TextInput(hint_text='Enter your walue (km)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Miles: ' + str(float(data) * 0.62)
            self.metres.text = 'Metres: ' + str(float(data) * 1000)
            self.santimetres.text = 'Santimetres: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def btn_pressed(self, *args):
        self.label.color = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.santimetres)
        # btn = Button(text='Touch Me')
        # btn.bind(on_press=self.btn_pressed)
        # box.add_widget(self.label)
        # box.add_widget(btn)
        return box


app = MyApp()
app.run()