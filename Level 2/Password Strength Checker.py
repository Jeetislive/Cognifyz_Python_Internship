# Task: Password Strength Checker
#
# Create a Python function that evaluates
# the strength of a password entered by the
# user. Implement checks for factors such as
# length, presence of uppercase and
# lowercase letters, digits, and special
# characters.

# Constraints:
# 1.password should contain 9 Letters
# 2.password must contain at least 1 upper case and 1 lower case
# 3.password may contain digits
# 4.password must not contain any special characters(except @,#,_)
def valid_password(p):
    # checking password for empty string
    if not p:
        return False
    # password should contain 9 Letters
    if len(p) < 9:
        print("Password must contain 9 letters!")
        return False
    # password must contain alphabets and some special characters
    valid = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#_")
    for i in p:
        if i not in valid:
            print(f"Password cannot contain {i}")
            return False
    # password must contain at least 1 upper case and 1 lower case
    uc = lc = 0
    li = [i for i in p if i.isalpha()]
    for i in li:
        if i.isupper():
            uc += 1
        else:
            lc += 1
    if uc < 1:
        print("Password must contain 1 uppercase character!")
        return False
    if lc < 1:
        print("Password must contain 1 lowercase character!")
        return False

    return True


password = input("Enter new password:")
if valid_password(password):
    print("Password stored successfully!")
else:
    print("Invalid Password!")
