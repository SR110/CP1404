class Band:
    """Represent a band object."""
    def __init__(self, name=""):
        """Initialize a band."""
        self.name = name
        self.musicians = []
        self.musicians_to_instruments = {}

    def __str__(self):
        """Return a string representation of a band object."""
        return f"{self.name} ({str(self.musicians).lstrip('[').rstrip(']')})"

    def add(self, member):
        """Add member to band."""
        self.musicians_to_instruments[member.name] = member.instruments
        self.musicians.append(f"{member.name} ({member.instruments})")

    def play(self):
        """Determine whether musician needs an instrument."""
        for musician in self.musicians_to_instruments:
            if not self.musicians_to_instruments[musician]:
                print(f"{musician} needs an instrument!")
            else:
                print(f"{musician} is playing: {self.musicians_to_instruments[musician][0]}")
