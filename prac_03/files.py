# 1) Write code that asks the user for their name,
# then opens a file called "name.txt" and
# writes that name to it. Remember to close your file.
OUTPUT_FILE = "name.txt"
name = input("Enter your name: ")

out_file = open(OUTPUT_FILE, "w")
out_file.write(name)
out_file.close()

# 2) (In the same file, but as if it were a separate program)
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
IN_FILE = "name.txt"
in_file = open(IN_FILE, "r")
content = in_file.read()
print(f"Your name is {content}")
in_file.close()

# 3) Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and
# adds them together then prints the result, which should be... 59.
IN_FILE = "numbers.txt"
in_file = open(IN_FILE, "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
result = first_number + second_number
print(f"Result is {result}")
in_file.close()

# 4) Now write a fourth block of code that prints the total for all lines in numbers.txt or
# a file with any number of numbers.
IN_FILE = "numbers.txt"
total = 0
in_file = open(IN_FILE, "r")
for line in in_file:
    number = int(line)
    total += number
print(f"Result is {total}")
in_file.close()
