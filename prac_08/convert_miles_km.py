from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

ONE_MILE = 1.60934


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy App to convert miles to km."""
    output = StringProperty()

    def build(self):
        """Build the Kivy App from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self, text):
        """Handle calculation."""
        value = self.validate_value(text)
        self.output = str(value * ONE_MILE)

    def handle_increment(self, text, change):
        """Handle buttons: Up and Down."""
        value = self.validate_value(text) + change
        self.root.ids.input_miles.text = str(value)

    def validate_value(self, text):
        """Change text into float."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKmApp().run()
