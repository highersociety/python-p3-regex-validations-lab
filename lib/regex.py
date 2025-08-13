import re

# NAME:
# - First and last names start with uppercase letters
# - Allows letters, apostrophes, hyphens, and prefixes like Mc
# - Requires exactly two words (first + last)
name = re.compile(
    r"^[A-Z][a-zA-Z'-]+ [A-Z][a-zA-Z'-]+$"
)

# PHONE NUMBER:
# - Allows optional country code (+1 or +44 etc.)
# - Handles (123) 456-7890, 123-456-7890, 123 456 7890
# - Allows +1-123-456-7890, +1 (123) 456-7890, etc.
phone_number = re.compile(
    r"^(\+\d{1,3}[- ]?)?(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$"
)