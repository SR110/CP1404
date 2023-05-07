import csv
from prac_06.guitar import Guitar


def main():
    guitar_list = []
    vintage_guitar_list = []
    new_guitar_list = []

    # Read in guitars from CSV file
    with open('guitars.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            guitar_list.append(Guitar(row[0], int(row[1]), float(row[2])))

    # Print out the list of guitars
    print("List of guitars:")
    for i, guitar in enumerate(guitar_list, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

    # Add new guitars to the list
    name = input("Enter the name of a new guitar (or 'q' to quit): ")
    while name != "q":
        year = int(input("Enter the year the guitar was made: "))
        cost = float(input("Enter the cost of the guitar: "))
        new_guitar = Guitar(name, year, cost)
        new_guitar_list.append(new_guitar)
        print(f"{new_guitar} added to the list.")
        name = input("Enter the name of a new guitar (or 'q' to quit): ")

    # Combine the original guitar list and the new guitar list
    guitar_list += new_guitar_list

    # Sort the list of guitars by year
    sorted_guitar_list = sorted(guitar_list, key=lambda x: x.year)

    # Print out the sorted list of guitars
    print("\nSorted list of guitars:")
    for i, guitar in enumerate(sorted_guitar_list, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

    # Write the list of guitars to the CSV file
    with open("guitars.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in sorted_guitar_list:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

    print(f"{len(new_guitar_list)} new guitar(s) added to the file.")


if __name__ == "__main__":
    main()
