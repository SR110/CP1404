MIN_LENGTH = 6


def main():
    """Validate password."""
    password = get_password()
    while len(password) < MIN_LENGTH:
        password = input("Enter password: ")
    display_asterisks(password)


def get_password():
    """Input password."""
    password = input("Enter password: ")
    return password


def display_asterisks(password):
    """Print asterisks."""
    print("*" * len(password))


main()