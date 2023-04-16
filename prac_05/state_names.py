"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# state_code = input("Enter short state: ").upper()


# "Look Before You Leap" Approach
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()


# "Easier to Ask Forgiveness than Permission" Approach
while True:
    try:
        state_code = input("Enter short state: ").upper()
        if not state_code:
            break
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")

for state_code in CODE_TO_NAME:
    print(f"{state_code:>3} is {CODE_TO_NAME[state_code]:>7}")
