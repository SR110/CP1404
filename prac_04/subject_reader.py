"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject details and display them."""
    subject_items = []
    data = get_data(subject_items)
    print(data)
    display_subject_details(subject_items)


def get_data(subject_items):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(",")
        subject_items.append(parts)
    input_file.close()
    return subject_items


def display_subject_details(subject_items):
    """Display details properly."""
    for subject_detail in subject_items:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]} and has {int(subject_detail[2])} students")


main()
