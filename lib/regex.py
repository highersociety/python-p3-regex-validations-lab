import re

# Name regex:
# - First letter uppercase
# - May contain lowercase letters
# - Apostrophe or hyphen may appear followed by uppercase + lowercase
# - One single space between name parts
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)*(?: [A-Z][a-z]*(?:['-][A-Z][a-z]*)*)*$"
)

# Phone regex:
# Matches:
# - 5555555555
# - 555-555-5555
# - (555) 555-5555
# No double dashes allowed
phone_regex = re.compile(
    r"^(?:\d{10}|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"
)

# Email regex:
# - Starts with letter
# - Local part can have letters, numbers, dots
# - Single @
# - Domain letters only, TLD at least 2 letters
email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]{2,}$"
)
