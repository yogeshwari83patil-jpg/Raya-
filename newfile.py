from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

responses = [
    "Hello human!",
    "How can I help you?",
    "You are amazing!",
    "Let's learn something new."
]

class AIApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.label = Label(text="Press the button to talk with AI 🤖")

        button = Button(text="Talk to AI")
        button.bind(on_press=self.talk)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def talk(self, instance):
        self.label.text = random.choice(responses)

AIApp().run()