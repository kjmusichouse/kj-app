from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

class ReviewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answers = []
        self.total = 0
        self.selected_topic = ""

    def on_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=10)
        scroll = ScrollView()

        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for idx, ans in enumerate(self.answers, 1):
            question_text = ans['question']
            selected_letter = ans['selected']
            correct_letter = ans['correct']
            options = ans['options']

            selected_index = ord(selected_letter) - ord('A')
            correct_index = ord(correct_letter) - ord('A')

            selected_text = options[selected_index] if 0 <= selected_index < len(options) else "N/A"
            correct_text = options[correct_index] if 0 <= correct_index < len(options) else "N/A"

            is_correct = selected_letter == correct_letter
            status_text = "CORRECT" if is_correct else "INCORRECT"
            status_color = "00ff00" if is_correct else "ff3333"

            text = f"[color=ffffff][b]{question_text}[/color]\n"
            text += f"[color=ffff00]Your Answer:[/color] [color=ffffff]{selected_text}[/color] [color={status_color}]{status_text}[/color]\n"

            if not is_correct:
                text += f"[color=00ff00]Correct Answer:[/color] [color=ffffff]{correct_text}[/color]"

            row = Label(
                text=text,
                markup=True,
                size_hint_y=None,
                height=dp(130),
                halign='left',
                valign='top'
            )
            row.bind(size=row.setter('text_size'))
            grid.add_widget(row)

        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)
