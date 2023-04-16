"""
Word Occurrences
Estimate: 20 minutes
Actual:   16 minutes
"""

word_to_occurrences = {}
string = input("Text: ")  # I am Shreya
words = string.split()  # ["I", "am", "Shreya"]
words.sort()
for i in range(len(words)):
    if words[i] not in word_to_occurrences:
        word_to_occurrences[words[i]] = 1
    else:
        word_to_occurrences[words[i]] += 1
for word in word_to_occurrences:
    print(f"{word:<10}: {word_to_occurrences[word]}", end="\n")
