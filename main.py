from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name = "main"))
        return sm

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Button(text= "Начать")
        boxl_horizontal = BoxLayout()
        boxl_horizontal_2 = BoxLayout()
        boxl_vertical = BoxLayout(orientation= "vertical")
        txt_1 = Label(text= "Заголовок")
        name = Label(text= "введите имя:")
        age = Label(text= "введите возраст:")
        boxl_vertical.add_widget(txt_1)
        boxl_vertical.add_widget(boxl_horizontal)
        boxl_horizontal.add_widget(name)
        boxl_vertical.add_widget(boxl_horizontal_2)
        boxl_horizontal_2.add_widget(age)
        boxl_vertical.add_widget(button)
        self.add_widget(boxl_vertical)

app = MyApp()
app.run()




























