from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App for demoing the Box Layout."""
    def build(self):
        """Build Kivy Application."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Call event handler when 'Greet' pressed."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Call event handler when 'Clear' pressed."""
        self.root.ids.input_label.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
