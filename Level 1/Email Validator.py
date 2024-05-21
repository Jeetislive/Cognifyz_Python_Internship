# Develop a Python function that validates
#  whether a given string is a valid email
#  address. Implement checks for the format,
#  including the presence of an "@" symbol and
#  a domain name

# Conditions:
# must have only one "@"
# username must contain only alphabet or numeric
# username must start with alphabet
# domain must contain only one "."

def valid_email(email):
    # checking email for empty string and only one @ in email
    if not email or '@' not in email or email.count('@') != 1:
        return False
    username, domain = email.split('@')
    # checking for username and domain length
    if len(username) == 0 or len(domain) < 9:
        return False
    # checking domain for only one . in domain
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False
    # checking if there is any white spaces in email
    if " " in email:
        return False
    # checking if username contain only alphanumeric characters or not
    for i in username:
        if not i.isalnum():
            return False
    # checking if username contain only alphanumeric characters except that one .
    for i in domain:
        if i.isalnum() or i == ".":
            return True
    return True


e = input("Enter the email for validation: ")
# Test cases
if valid_email(e):
    print("Your Email is valid")
else:
    print("Invalid Email!")
