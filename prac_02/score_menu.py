MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""
score = int(input("score:"))


def main(score):
    """Display menu."""
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score(score)
        elif choice == "P":
            grades = get_score(score)
            print(grades)
        elif choice == "S":
            stars(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you")


def validate_score(score):
    """Check whether score is valid."""
    while score < 0 or score > 100:
        print("invalid score")
        score = int(input("score:"))
    return score


def get_score(score):
    """Determine grade."""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"


def stars(score):
    """Display star."""
    print("*" * score)


main(score)
