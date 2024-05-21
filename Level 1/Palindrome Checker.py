# Task: Palindrome Checker
#  Write a Python function that checks whether
#  a given string is a palindrome. A palindrome
#  is a word, phrase, or sequence that reads the
#  same backward as forward (e.g., "madam" or
#  "racecar")

def palindrome_check(s):
    # checking whether the reverse of given string is equals to original
    if s == s[::-1]:
        return True
    return False


p = input("Enter string to check palindrome or not:")
if len(p) > 1:
    if palindrome_check(p):
        print(f"{p} is a palindrome string")
    else:
        print(f"{p} is not a palindrome string")
else:
    print("Given string has not enough length to check Palindrome or Not")
