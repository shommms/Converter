#Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

#Глобальные настройки
Window.size = (250,250)
Window.title = "Конвертер"

class MainApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text = "Конвертер")
        self.milmeters = Label (text = "Миллиметры")
        self.metres = Label (text = "Метры")
        self.dm = Label(text = "ДициМетры")
        self.kilometr = Label(text = "Километр")
        self.input_data = TextInput(hint_text = "Введите значение в см",multiline = False)
        self.input_data.bind(text=self.on_text)
    #Данные и их конвертация
    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.milmeters.text = 'Миллиметры: '+str(float(data)*10)
            self.metres.text = 'Метры: '+str(float(data)/100)
            self.kilometr.text = 'Километр: '+str(float(data)/100000)
            self.dm.text = 'ДициМетры: '+str(float(data)/10)
            
        else:
            self.input_data.text = ""
            self.milmeters.text = 'Миллиметры'
            self.metres.text = 'Метры'
            self.metres.text = 'Километр'
            
    #Основной метод программы
    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.milmeters)
        box.add_widget(self.dm)
        box.add_widget(self.metres)
        box.add_widget(self.kilometr)

        return box

app = MainApp()
app.run()