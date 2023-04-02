MENU = """
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
"""


def main():
    """Convert unit of temperature."""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(result))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            result = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(result))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Program over")


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    output = celsius * 9.0 / 5 + 32
    return output


def fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    output = 5 / 9 * (fahrenheit - 32)
    return output


main()
