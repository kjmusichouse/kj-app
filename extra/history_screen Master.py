# FILE: screens/history_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from datetime import datetime
import json
import os


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history_file = 'data/history.json'
        self.units_data = self.load_units_and_chapters()
        self.topics_data = self.load_biology_topics()

    def load_units_and_chapters(self):
        units = {}
        current_unit = ""
        current_chapter = ""

        with open('data/Units_Chapters.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("UNIT"):
                    current_unit = line
                    units[current_unit] = {}
                elif line.lower().startswith("chapter"):
                    parts = line.split(':')
                    if len(parts) >= 2:
                        chapter_num = parts[0].split()[1]
                        chapter_name = parts[1].strip()
                        current_chapter = chapter_name.lower().replace(' ', '_')
                        if current_unit:
                            units[current_unit][current_chapter] = []
        return units

    def load_biology_topics(self):
        topics = {}
        current_chapter = ""
        with open('data/biology_topics.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    current_chapter = line[1:-1].strip().lower().replace(' ', '_')
                elif line and not line.lower().startswith('summary'):
                    if current_chapter not in topics:
                        topics[current_chapter] = []
                    topics[current_chapter].append(line)
        return topics

    def on_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=dp(10))
        scroll = ScrollView()
        outer_grid = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        outer_grid.bind(minimum_height=outer_grid.setter('height'))

        history_data = {}
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                for entry in json.load(f):
                    topic = entry['topic']
                    if topic not in history_data:
                        history_data[topic] = []
                    history_data[topic].append(entry)

        # sort history inside each topic
        for topic_list in history_data.values():
            topic_list.sort(key=lambda x: x['date'], reverse=True)

        for unit, chapters in self.units_data.items():
            outer_grid.add_widget(Label(
                text=f"[b]{unit}[/b]",
                markup=True,
                size_hint_y=None,
                height=dp(40),
                color=get_color_from_hex("#00ffff")
            ))

            for chapter_key in chapters:
                outer_grid.add_widget(Label(
                    text=f"[color=ffff00]{chapter_key.replace('_', ' ').title()}[/color]",
                    markup=True,
                    size_hint_y=None,
                    height=dp(30)
                ))

                chapter_topics = self.topics_data.get(chapter_key, [])
                for topic in chapter_topics:
                    latest = history_data.get(topic, [{}])[0]
                    result = latest.get('result', 'N/A')
                    performance = latest.get('performance', 'Pending')
                    raw_date = latest.get('date', '---')
                    # Reformat date
                    try:
                        date_obj = datetime.strptime(raw_date, "%Y-%m-%d %H:%M")
                        formatted_date = date_obj.strftime("%d-%m-%Y %I:%M %p")
                    except:
                        formatted_date = raw_date


                    row = GridLayout(cols=5, spacing=dp(5), size_hint_y=None, height=dp(40))
                    row.add_widget(Label(text=topic, color=[1, 1, 1, 1]))
                    row.add_widget(Label(text=result))
                    row.add_widget(Label(text=performance))
                    row.add_widget(Label(text=formatted_date))

                    view_btn = Button(text='View', size_hint_x=None, width=dp(80))
                    view_btn.bind(on_release=lambda btn, t=topic: self.view_review(t))
                    row.add_widget(view_btn)

                    outer_grid.add_widget(row)

        scroll.add_widget(outer_grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def view_review(self, topic_name):
        review_screen = self.manager.get_screen('review')
        review_screen.load_topic_from_history(topic_name)
        self.manager.current = 'review'
