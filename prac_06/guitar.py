"""Estimated time - 15 minutes
Actual time - 10 minutes
"""

YEAR_NOW = 2023
VINTAGE_AGE = 50


class Guitar:
    """Record details of one Guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise the details of a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get age of Guitar with respect to current year."""
        return YEAR_NOW - self.year

    def is_vintage(self):
        """Check whether Guitar is vintage or not."""
        return self.get_age() >= 50
