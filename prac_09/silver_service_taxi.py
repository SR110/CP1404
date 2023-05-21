from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string representation of a Silver Service Taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = self.flagfall + super().get_fare()
        return fare
