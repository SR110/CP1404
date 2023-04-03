"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # 3) Yes, code is given below (line 13 and 14)
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
    # 1) ValueError occurs when numerator and denominator are not of integer type (in this case)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    # 2) ZeroDivisionError occurs when the denominator is zero
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
