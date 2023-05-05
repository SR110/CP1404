"""Estimated time - 20 minutes
Actual time - 20 minutes
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

guitar_name = input("Name: ")
while guitar_name != "":
    year = input("Year: ")
    cost = float(input("Cost: $"))
    guitar_to_include = Guitar(guitar_name, year, cost)
    guitars.append(guitar_to_include)
    print(guitar_to_include, "added.")
    guitar_name = input("Guitar name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

if guitars:
    guitars.sort()
    print("These are the guitars that I own: ")
    for index, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {index}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
else:
    print("You don't have any guitars!")