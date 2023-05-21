from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Represent an unreliable car object."""
    def __init__(self, name="", fuel=0, reliability=0.0):
        """Initialise an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car according to reliability."""
        if random.randint(1, 100) >= self.reliability:
            distance = 0
        distance_covered = super().drive(distance)
        return distance_covered
