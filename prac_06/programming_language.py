"""Estimated time - 20 minutes
Actual time - 30 minutes
"""


class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        """Initialise the Programming Language."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return representation of a Programming Language."""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check whether typing of Programming Language is dynamic or not."""
        return self.typing == "Dynamic"
