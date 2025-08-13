import re

# Matches names like "John Cena", "D'Angelo", "Anya Taylor-Joy"
name_regex = re.compile(
    r"^[A-Z][a-z]+(?:['-][A-Z][a-z]+)*(?: [A-Z][a-z]+(?:['-][A-Z][a-z]+)*)*$"
)

# Matches phone formats: "5555555555", "555-555-5555", "(555) 555-5555"
phone_regex = re.compile(
    r"^(?:\(\d{3}\)\s|\d{3}-)?\d{3}-?\d{4}$"
)

# Matches emails like "john.cena@wwe.com", "john.cena123@wwe.com"
email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]{2,}$"
)
