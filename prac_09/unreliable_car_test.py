from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable cars."""
    good_car = UnreliableCar("Lamborghini", 100, 85.0)
    bad_car = UnreliableCar("Maruti 800", 100, 10.0)

    for index in range(1, 5):
        print(f"For a distance of {index}km: ")
        print(f"{good_car.name:10} drove {good_car.drive(index):3}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(index):3}km")

    print(good_car)
    print(bad_car)


main()
