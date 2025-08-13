import re

# Matches names with only letters and spaces (no numbers or special chars)
# Allows multiple words (e.g., "John Doe", "Mary Ann Smith")
name_regex = r"^[A-Za-z]+(?: [A-Za-z]+)*$"

# Matches phone numbers with optional + at start, then 10–15 digits
# Example: +254712345678, 0712345678
phone_regex = r"^\+?[0-9]{10,15}$"

# Matches standard emails: letters/numbers, dots, hyphens allowed before @ and domain
email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
