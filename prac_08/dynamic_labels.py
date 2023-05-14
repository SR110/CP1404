from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelApp is a Kivy App to create a separate label for each name."""
    def __init__(self, **kwargs):
        """Define list of names."""
        super().__init__(**kwargs)
        self.names = ['Alice', 'Sasha', 'Susan', 'Natasha', 'Anna', 'Samantha']

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """list names."""
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.label_box.add_widget(temp_button)


DynamicLabelsApp().run()
