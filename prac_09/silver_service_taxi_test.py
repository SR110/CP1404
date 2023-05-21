from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxis."""
    taxi = SilverServiceTaxi("Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()
