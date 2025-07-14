from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BiologyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_class = None  # will be set from SubjectScreen

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        study_btn = Button(text="Study Material", font_size=24)
        study_btn.bind(on_press=self.open_study_material)

        quiz_btn = Button(text="Quiz", font_size=24)
        quiz_btn.bind(on_press=self.open_quiz)

        layout.add_widget(study_btn)
        layout.add_widget(quiz_btn)

        self.add_widget(layout)

    def open_study_material(self, instance):
        # Placeholder action for now
        print("📘 Study Material Clicked")

    def open_quiz(self, instance):
        chapter_screen = self.manager.get_screen('chapter_list')
        chapter_screen.selected_class = self.selected_class
        chapter_screen.selected_subject = 'biology'
        self.manager.current = 'chapter_list'
