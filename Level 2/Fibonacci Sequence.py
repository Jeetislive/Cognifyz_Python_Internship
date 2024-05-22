# Task: Fibonacci Sequence
#
# Write a Python function that generates the
# Fibonacci sequence up to a given number of
# terms. The function should take an integer
# input from the user and display the
# Fibonacci sequence up to that number of
# terms.
def fibonacci_sequence(n) -> list:
    li = []
    n1, n2 = 0, 1
    li.append(n1)
    li.append(n2)
    for i in range(0, n - 2):
        temp = n2
        n2 = n1 + n2
        n1 = temp
        li.append(n2)
    return li


f = int(input("Enter the number up to you want the Fibonacci series:"))
print(fibonacci_sequence(f))
