import re

# NAME:
# - First and last names start with uppercase letters
# - Allows letters, apostrophes, hyphens, and prefixes like Mc
# - Requires exactly two words (first + last)
name = re.compile(
    r"^[A-Z][a-zA-Z'-]+ [A-Z][a-zA-Z'-]+$"
)
