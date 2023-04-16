"""
Emails
Estimate: 28 minutes
Actual:   21 minutes
"""

def main():
    """Make dictionary of email to name."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "Y" and choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    """Get name from email."""
    first_part = email.split("@")[0]   # lindsay.ward
    names = first_part.split(".")
    full_name = " ".join(names).title()
    return full_name

main()

