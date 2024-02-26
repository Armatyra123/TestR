from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from instr import *
from kivy.properties import BooleanProperty
from kivy.clock import Clock


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ForthScreen(name="rest_screen"))
        sm.add_widget(FirstScreen(name="main"))
        sm.add_widget(SecondScreen(name="pulse_screen"))
        sm.add_widget(ThirdScreen(name="sit_screen"))
        return sm


class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        self.done = False
        text = f"Прошло секунд: {self.current}"
        super().__init__(text=text, **kwargs)

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def restart(self, total):
        self.done = False
        self.total = total
        self.current = 0
        self.text = f"Прошло секунд: {self.current}"
        self.start()

    def change(self, dt):
        self.current += 1
        self.text = f"Прошло секунд: {self.current}"
        if self.current >= self.total:
            self.done = True
            return False


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        button.on_press = self.next
        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(multiline=False)
        boxl_horizontal = BoxLayout(size_hint=(0.8, None), height="30sp")
        boxl_horizontal_2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        boxl_vertical = BoxLayout(orientation="vertical", spacing=4, padding=9)
        txt_1 = Label(text=txt_instruction)
        name = Label(text="введите имя:")
        age = Label(text="введите возраст:")
        boxl_vertical.add_widget(txt_1)
        boxl_vertical.add_widget(boxl_horizontal)
        boxl_horizontal.add_widget(name)
        boxl_horizontal.add_widget(self.name_input)
        boxl_vertical.add_widget(boxl_horizontal_2)
        boxl_horizontal_2.add_widget(age)
        boxl_horizontal_2.add_widget(self.age_input)
        boxl_vertical.add_widget(button)
        self.add_widget(boxl_vertical)

    def next(self):
        try:
            age = int(self.age_input.text)
            if 7 <= age <= 100:
                self.manager.current = "pulse_screen"
            else:
                self.age_input.text = "50"
        except ValueError:
            self.age_input.text = "Только цифры!"

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.button = Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.button.on_press = self.next
        self.result = TextInput(multiline=False, size_hint=(0.9, None), height="30sp", pos_hint={'center_y': 0.5})
        self.result.disabled = True
        boxl_horizontal = BoxLayout(size_hint=(1, None), height="100sp")
        boxl_vertical = BoxLayout(orientation="vertical", spacing=4, padding=9)
        txt_1 = Label(text=txt_test1, size_hint=(1, None), height="350sp", pos_hint={"center_y": 0.1})
        user_input = Label(text="Введите результат:")
        self.timer = Timer(15, size_hint=(1, None), height="30sp", pos_hint={"center_y": 0.1})
        self.timer.bind(done=self.end)
        boxl_vertical.add_widget(txt_1)
        boxl_vertical.add_widget(self.timer)
        boxl_vertical.add_widget(boxl_horizontal)
        boxl_horizontal.add_widget(user_input)
        boxl_horizontal.add_widget(self.result)
        boxl_vertical.add_widget(self.button)
        self.add_widget(boxl_vertical)

    def end(self, *args):
        self.next_screen = True
        self.button.disabled = False
        self.result.disabled = False

    def next(self):
        if self.next_screen:
            try:
                pulse = int(self.result.text)
                if 1 <= pulse <= 250:
                    self.manager.current = "sit_screen"
                else:
                    self.result.text = "Ты там живой вообще?"
            except ValueError:
                self.result.text = "Только цифры!"
        else:
            self.timer.start()
            self.button.disabled = True

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Button(text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        button.on_press = self.next
        txt = Label(text=txt_sits)
        boxl_vertical = BoxLayout(orientation="vertical", spacing=4, padding=9)
        boxl_vertical.add_widget(txt)
        boxl_vertical.add_widget(button)
        self.add_widget(boxl_vertical)

    def next(self):
        self.manager.current = "rest_screen"


class ForthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_m = False
        self.button = Button(text="Завершить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.button.on_press = self.next
        self.result = TextInput(multiline=False)
        self.result.disabled = True
        self.rest_result = TextInput(multiline=False)
        self.rest_result.disabled = True
        boxl_horizontal = BoxLayout(size_hint=(0.8, None), height="30sp")
        boxl_horizontal_2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        boxl_vertical = BoxLayout(orientation="vertical", spacing=4, padding=9)
        txt_1 = Label(text=txt_test3)
        self.timer = Timer(15, size_hint=(1, None), height="30sp", pos_hint={"center_y": 0.1})
        self.timer.bind(done=self.end)
        self.stage = 0
        result = Label(text="Результат:")
        rest_result = Label(text="Результат после отдыха:")
        boxl_vertical.add_widget(txt_1)
        boxl_vertical.add_widget(self.timer)
        boxl_vertical.add_widget(boxl_horizontal)
        boxl_horizontal.add_widget(result)
        boxl_horizontal.add_widget(self.result)
        boxl_vertical.add_widget(boxl_horizontal_2)
        boxl_horizontal_2.add_widget(rest_result)
        boxl_horizontal_2.add_widget(self.rest_result)
        boxl_vertical.add_widget(self.button)
        self.add_widget(boxl_vertical)

    def end(self, *args):
        if self.timer.done:
            if self.stage == 0:
                self.stage = 1
                self.timer.restart(30)
                self.result.disabled = False
            elif self.stage == 1:
                self.timer.restart(15)
                self.stage = 2
                print("я работаю")
            elif self.stage == 2:
                self.next_m = True
                self.rest_result.disabled = False
                self.button.disabled = False
            print("adflkmweflkmdf")

    def next(self):
        if self.next_m:
            try:
                result = int(self.result.text)
                if 1 <= result <= 500:
                    try:
                        rest_result = int(self.rest_result.text)
                        if 1 <= result <= 500:
                            pass
                        else:
                            self.rest_result.text = "Ты живой?"
                    except ValueError:
                        self.rest_result.text = "Только цифры!"
                else:
                    self.result.text = "Ты живой?"
            except ValueError:
                self.result.text = "Только цифры!"
        else:
            self.timer.start()
            self.button.disabled = True

app = MyApp()
app.run()






























