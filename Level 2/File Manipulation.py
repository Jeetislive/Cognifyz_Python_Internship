# Task: File Manipulation
#
# Write a Python program that reads a text
# file and counts the occurrences of each
# word in the file. Display the results in
# alphabetical order along with their
# respective counts.
from collections import defaultdict
try:
    with open("Text.txt") as file:
        word_counts = defaultdict(int)
        for i in file:
            words = i.split()
        # print(words)
        for i in words:
            word_counts[i] += 1
        sorted_words = sorted(word_counts.items())
        for i, c in sorted_words:
            print(f"{i}: {c}")
        # print(file.read())
except FileNotFoundError:
    print("That file was not found!")
