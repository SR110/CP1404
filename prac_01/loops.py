# odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# a)
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b)
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c)
number = int(input("Enter the number of stars: "))
for i in range(0, number):
    print("*", end="")
print()

# d)
for i in range(1, number + 1):
    print("*" * i)
