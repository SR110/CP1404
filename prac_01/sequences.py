MENU = """
i.   Show the even numbers from x to y
ii.  Show the odd numbers from x to y
iii. Show the squares from x to y
iv.  Exit the program
"""

print(MENU)
choice = input("Enter the choice: ")
x = int(input("Enter the smaller number: "))
y = int(input("Enter the bigger number: "))

if choice == "i":
    if x < y:
        if x % 2 == 0:
            for j in range(x, y+1, 2):
                print("The even numbers from x to y is ", j)
        else:
            for j in range(x+1, y+1, 2):
                print("The even numbers from x to y is ", j)

elif choice == "ii":
    if x < y:
        if x%2 != 0:
            for j in range(x, y+1, 2):
                print("The odd numbers from x to y is ", j)
        else:
            for j in range(x+1, y+1, 2):
                print("The odd numbers from x to y is ", j)

elif choice == "iii":
    if x < y:
        for j in range(x, y+1):
            square_root = j**0.5
            if isinstance(square_root, int):
                print("The squares from x to y are", j)

elif choice == "iv":
    print("Exit the program.")

else:
    print("Invalid Choice!")