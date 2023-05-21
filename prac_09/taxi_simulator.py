from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive
"""


def main():
    """Display MENU."""
    nett_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                nett_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${nett_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${nett_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of taxis neatly."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def conduct_tests():
    """Run tests to show workings of Car and Taxi classes."""
    truck = Car("Volvo", 180)
    truck.drive(30)
    print("fuel =", truck.fuel)
    print("odo =", truck._odometer)
    truck.drive(55)
    print("fuel =", truck.fuel)
    print("odo = ", truck._odometer)
    print(truck)

    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_travelled = truck.drive(distance)
        print(f"{truck} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    taxi = Taxi("Limo", 100)
    print(taxi)
    taxi.drive(25)
    print(taxi, taxi.get_fare())
    taxi.start_fare()
    taxi.drive(40)
    print(taxi, taxi.get_fare())

    sst = SilverServiceTaxi("Prius", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


# conduct_tests()
main()