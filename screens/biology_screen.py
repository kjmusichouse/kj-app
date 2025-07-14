from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp


class BiologyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None  # set from previous screen

        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(40))

        study_btn = Button(text="Study Material", font_size=24, size_hint_y=None, height=dp(60))
        study_btn.bind(on_press=self.open_study_material)

        quiz_btn = Button(text="Quiz", font_size=24, size_hint_y=None, height=dp(60))
        quiz_btn.bind(on_press=self.open_quiz)

        history_btn = Button(text="History", font_size=24, size_hint_y=None, height=dp(60))
        history_btn.bind(on_press=self.open_history)

        layout.add_widget(study_btn)
        layout.add_widget(quiz_btn)
        layout.add_widget(history_btn)

        self.add_widget(layout)

    def open_study_material(self, instance):
        print("📘 Study Material Clicked")

    def open_quiz(self, instance):
        chapter_screen = self.manager.get_screen('chapter_list')
        chapter_screen.selected_class = self.selected_class
        chapter_screen.selected_subject = 'biology'
        self.manager.current = 'chapter_list'

    def open_history(self, instance):
        history_screen = self.manager.get_screen('history_screen')
        history_screen.selected_class = self.selected_class
        history_screen.selected_subject = 'biology'
        #history_screen.load_history()  # Optional: refresh history view
        self.manager.current = 'history_screen'
