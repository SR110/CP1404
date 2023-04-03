import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Ans:- : prints any random integer from 5 to 20, including 5 and 20 eg: 14
# What was the smallest number you could have seen, what was the largest?
# Ans:- smallest number = 5,
#       largest number = 20

# What did you see on line 2?
# Ans:- prints any random integer from the list, [3,5,7,9] eg: 9
# What was the smallest number you could have seen, what was the largest?
# Ans:- smallest number = 3
#       largest number = 9
# Could line 2 have produced a 4?
# Ans:- No, because the step value is 2. So, it starts from 3 and the next value is 3+2 = 5

# What did you see on line 3?
# Ans:- : prints any random floating point number between 2.5 and 5.5, both included
# What was the smallest number you could have seen, what was the largest?
# Ans:- smallest number = 2.5
#       largest number = 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
