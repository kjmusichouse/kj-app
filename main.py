from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# Importing all screens
from screens.home_screen import HomeScreen
from screens.subject_screen import SubjectScreen
from screens.biology_screen import BiologyScreen
from screens.chapter_list_screen import ChapterListScreen
from screens.topic_list_screen import TopicListScreen
from screens.quiz_screen import QuizScreen
from screens.result_screen import ResultScreen
from screens.review_screen import ReviewScreen
from screens.history_screen import HistoryScreen


class QuizApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SubjectScreen(name='subject'))
        sm.add_widget(BiologyScreen(name='biology'))
        sm.add_widget(ChapterListScreen(name='chapter_list'))
        sm.add_widget(ChapterListScreen(name='chapter_list_screen'))
        sm.add_widget(TopicListScreen(name='topic_list'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(ReviewScreen(name='review'))
        sm.add_widget(HistoryScreen(name='history_screen'))

        return sm



if __name__ == '__main__':
    QuizApp().run()
