# Task: Number Guesser
#
# Create a number guessing game where the
# program generates a random number
# between a specified range, and the user tries
# to guess it. Provide feedback to the user if
# their guess is too high or too low.
import random as r
print("Enter a range in which you want to play the Number Guessing game:")
a, b = int(input("Enter lower limit:")), int(input("Enter upper limit:"))
n = r.randint(a, b)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == n:
        print("Congratulation! You got the number")
        break
    elif guess > n:
        print("too high! Try again")
    else:
        print("too low! Try again")


