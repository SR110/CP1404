FILENAME = "wimbledon.csv"


def read_wimbledon_data():
    """Read Wimbledon data from a CSV file."""
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        header = file.readline().strip().split(",")  # skip the header
        data = [line.strip().split(",") for line in file]
    return header, data


def get_champions(data, champion_column=2):
    """Count number of championships won by each player."""
    champion_to_count = {}
    for row in data:
        player = row[champion_column]
        if player in champion_to_count:
            champion_to_count[player] += 1
        else:
            champion_to_count[player] = 1
    return champion_to_count


def get_countries(data, country_column=1):
    """Get a set of countries that have won Wimbledon."""
    countries = set()
    for row in data:
        country = row[country_column]
        countries.add(country)
    return countries


def display_champions(champions):
    """Display number of championships won by each player."""
    print("Wimbledon Champions:")
    for player, count in champions.items():
        print(player, count)


def display_countries(countries):
    """Display countries that have won Wimbledon."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def main():
    """Read data, process it, and display results."""
    header, data = read_wimbledon_data()
    champions = get_champions(data)
    countries = get_countries(data)
    display_champions(champions)
    display_countries(countries)


main()
