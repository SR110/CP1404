"""Estimated time - 12 minutes
Actual time - 10 minutes
"""
from prac_06.guitar import Guitar
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
guitar1 = Guitar(name, year, cost)
guitar2 = Guitar("Another Guitar", 2022, 1499.99)

print(f"{guitar1.name} get_age() - Expected 101. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 1. Got {guitar2.get_age()}")

print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
