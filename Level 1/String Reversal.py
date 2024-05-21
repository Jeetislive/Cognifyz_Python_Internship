# Task: String Reversal
# Create a Python function that takes a string as
# input and returns the reverse of that string.
# For example, if the input is "hello,"
# the function should return "olleh."
def string_reversal(s):
    if s != '':
        return s[::-1]
    return "Given string is a empty string"


n = input("Enter a String to be reversed:")
print(string_reversal(n))
