import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

email = input("Enter an email address: ")
result = validate_email(email)
print(result)