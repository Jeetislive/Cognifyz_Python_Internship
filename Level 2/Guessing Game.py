# Task: Guessing Game
#
# Write a Python program that generates a
# random number between 1 and 100. The
# user should then try to guess the number.
# The program should provide hints such as
# "too high" or "too low" until the correct
# number is guessed.

import random as r
n = r.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == n:
        print("Congratulation! You got the number")
        break
    elif guess > n:
        print("too high! Try again")
    else:
        print("too low! Try again")

