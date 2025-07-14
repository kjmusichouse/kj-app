from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        for cls in ['Class 10', 'Class 11', 'Class 12']:
            btn = Button(text=cls, font_size=24)
            btn.bind(on_press=self.on_class_selected)
            layout.add_widget(btn)

        self.add_widget(layout)

    def on_class_selected(self, instance):
        selected_class = instance.text.split()[-1]
        self.manager.get_screen('subject').selected_class = selected_class
        self.manager.current = 'subject'
