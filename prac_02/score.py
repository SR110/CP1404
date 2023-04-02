import random

def main():
    """Input score."""
    score = float(input("Enter score: "))
    grades = get_grade(score)
    print(grades)
    print(f"The random score is", get_grade(random.randint(0, 100)))


def get_grade(score):
    """Determine grade."""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()