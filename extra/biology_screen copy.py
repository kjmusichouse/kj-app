from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BiologyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        chapter_btn = Button(text="Select Chapter")
        chapter_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'chapter_list'))

        history_btn = Button(text="History")
        history_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'history'))

        layout.add_widget(chapter_btn)
        layout.add_widget(history_btn)

        self.add_widget(layout)
